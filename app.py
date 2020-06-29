from flask import (
    Flask,
    render_template,
    flash,
    jsonify,
    request,
    url_for,
    make_response,
    request,
    redirect,
    abort,
)
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length
from mpdetails import validate_postcode_api
from emailtemplates import (
    get_templates_by_topic,
    get_templates_by_slug,
    get_existing_templates,
    draft_templates,
)
from urllib import parse
from secrets import token_bytes
from address import get_addresses
from slugify import slugify
from requests.exceptions import HTTPError

import json
import logging
import os
import sys
import requests
import hashlib

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

try:
    skey = bytes(os.environ["FLASK_SECRET_KEY"], "utf-8")
except KeyError:
    # Testing environment
    skey = token_bytes(16)

app.secret_key = skey


""" For developers running on a newer version of openssl:
    A recent update to openssl was pushed to fix something
    called a logjam attack. The ciphers that are being used
    in some of the libs mustn't be up to date yet which
    may cause errors when running the server in a dev env.
    This try/catch bypasses the requirement of a longer key.
"""
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += "HIGH:!DH:!aNULL"
try:
    requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += (
        "HIGH:!DH:!aNULL"
    )
except AttributeError:
    # no pyopenssl support used / needed / available
    pass


url = "https://us10.api.mailchimp.com/3.0/lists/{}/members/".format(
    os.environ["MCLIST_ID"]
)


@app.before_request
def force_https():
    criteria = [
        app.debug,
        request.is_secure,
        request.headers.get("X-Forwarded-Proto", "http") == "https",
    ]

    if not any(criteria):
        if request.url.startswith("http://"):
            url = request.url.replace("http://", "https://", 1)
            code = 301
            r = redirect(url, code=code)
            return r


@app.errorhandler(404)
def error_404(error):
    return render_template("404.html", error=error), 404


@app.route("/", methods=["GET", "POST"])
def landing():

    if request.method == "GET":
        return render_template("landing.html")
    else:
        name = request.form["name"]
        postcode = request.form["postcode"].replace(" ", "")
        address = request.form.get("address")
        empty_templates = get_existing_templates()
        emails = draft_templates(empty_templates, name, postcode, address)
        return render_template("all-topics.html", emails=emails)


@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")


@app.route("/postcode/<postcode>")
def postcode(postcode):
    # ToDo : Re-use this postcode query for MP data gathering
    post_code_data = validate_postcode_api(postcode)
    if post_code_data["status"] == 200:
        return json.dumps(get_addresses(postcode))
    else:
        return make_response({"error": "Invalid postcode"}, 400)


@app.route("/topic/<topic>", methods=["GET", "POST"])
def landing_single_topic(topic):
    matching_templates = get_templates_by_topic(topic)
    if len(matching_templates) == 0:
        abort(404, "Topic not found")
    else:
        if request.method == "GET":
            # ToDo: Need to make a topic-specific landing page
            return render_template("landing.html")
        else:
            name = request.form["name"]
            postcode = request.form["postcode"].replace(" ", "")
            address = request.form.get("address")
            emails = draft_templates(matching_templates, name, postcode, address)
            topic_capitalised = topic.replace("-", " ").title()
            return render_template(
                "single-topic.html", emails=emails, topic=topic_capitalised
            )


@app.route("/template/<template_slug>", methods=["GET", "POST"])
def display_template(template_slug):
    matching_templates = get_templates_by_slug(slugify(template_slug))
    if len(matching_templates) == 0:
        abort(404, "Topic not found")
    else:
        if request.method == "GET":
            return render_template("landing.html")
        else:
            name = request.form["name"]
            postcode = request.form["postcode"].replace(" ", "")
            address = request.form.get("address")
            email_template = draft_templates(
                matching_templates, name, postcode, address
            )
            return render_template("single_email.html", email=email_template[0])


@app.route("/newsletter/subscribe", methods=["POST"])
def subscribe_to_newsletter():

    post_params = {"email_address": request.form["email"], "status": "subscribed"}
    r = requests.post(
        url, auth=("foo", os.environ["MAILCHIMP_SECRET_KEY"]), json=post_params
    )
    try:
        r.raise_for_status()
    except HTTPError:
        return jsonify(status="failed")

    return jsonify(status="success")


@app.route("/newsletter/check", methods=["POST"])
def check_user_newsletter():

    print(request.form)
    email = request.form["email"].encode("utf-8")
    user_hash = hashlib.md5(email).hexdigest()
    req_url = "{}{}".format(url, user_hash)
    print(req_url)
    r = requests.get(req_url, auth=("foo", os.environ["MAILCHIMP_SECRET_KEY"]))
    try:
        r.raise_for_status()
    except HTTPError:
        return jsonify(status="failed")

    return jsonify(status="success", action=request.form["action"], user=user_hash)


@app.route("/newsletter/unsubscribe", methods=["POST"])
def unsubscribe_user_newsletter():
    print(request.form)
    req_url = "{}{}".format(url, request.form["user"])
    print(req_url)
    r = requests.delete(req_url, auth=("foo", os.environ["MAILCHIMP_SECRET_KEY"]))
    try:
        r.raise_for_status()
    except HTTPError:
        return jsonify(status="failed")

    return jsonify(status="success")


@app.route("/newsletter/permanently_delete", methods=["POST"])
def permanently_delete_user_newsletter():

    print(request.form)
    req_url = "{}{}/actions/delete-permanent".format(url, request.form["user"])
    print(req_url)
    r = requests.post(req_url, auth=("foo", os.environ["MAILCHIMP_SECRET_KEY"]))
    try:
        r.raise_for_status()
    except HTTPError:
        return jsonify(status="failed")

    return jsonify(status="success")

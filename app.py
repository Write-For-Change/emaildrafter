from flask import Flask, render_template, flash, jsonify, request, url_for, make_response, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length
from emails import draftEmails, validatePostcodeApi
from urllib import parse
from secrets import token_bytes
from address import getAddresses

import json
import logging
import os
import sys

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

try:
    skey = bytes(os.environ['FLASK_SECRET_KEY'], 'utf-8')
except KeyError:
    # Testing environment
    skey = token_bytes(16)

app.secret_key = skey

@app.before_request
def force_https():
        criteria = [
            app.debug,
            request.is_secure,
            request.headers.get('X-Forwarded-Proto', 'http') == 'https',
        ]

        if not any(criteria):
            if request.url.startswith('http://'):
                url = request.url.replace('http://', 'https://', 1)
                code = 301
                r = redirect(url, code=code)
                return r

@app.route("/", methods=["GET", "POST"])
def landing():

    if request.method == "GET":
        return render_template("landing.html")
    else:
        name = request.form["name"]
        postcode = request.form["postcode"].replace(" ", "")
        address = request.form.get("address")
        emails = draftEmails(name, postcode, address)
        a = [
            {
                "email": (e.target["email"]),
                "subject_coded": parse.quote(e.subject),
                "body_coded": parse.quote(e.body).replace("%0A", "%0D%0A"),
                "subject": (e.subject),
                "body": (e.body),
            }
            for e in emails
        ]
        # return jsonify(a)
        return render_template("emails.html", emails=a)


@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/postcode/<postcode>")
def postcode(postcode):
    if validatePostcodeApi(postcode):
        return json.dumps(getAddresses(postcode))
    else:
        return make_response({"error": "Invalid postcode"}, 400)

from flask import Flask, render_template, flash, jsonify, request, url_for, make_response
from flask_talisman import Talisman
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

try:
    skey = bytes(os.environ['FLASK_SECRET_KEY'], 'utf-8')
except KeyError:
    # Testing environment
    skey = token_bytes(16)

app = Flask(__name__)
app.secret_key = skey

csp = {
    'default-src': '\'self\'',
    'img-src': '*',
    'media-src': '*',
    'script-src': '*'
}

Talisman(app, strict_transport_security=False, content_security_policy=csp)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

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
                "body_coded": parse.quote(e.body),
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

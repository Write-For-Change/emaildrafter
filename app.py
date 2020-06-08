from flask import Flask, render_template, flash, jsonify, request, url_for, make_response, redirect
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from emails import draftEmails, validatePostcodeApi#, createTemplate
from urllib import parse
from secrets import token_bytes
from address import getAddresses

import emailtemplates
import json
import logging
import os
import sys

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

try:
    skey = bytes(os.environ['FLASK_SECRET_KEY'], 'utf-8')

    app.config['RECAPTCHA_PUBLIC_KEY'] = os.environ['RECAPTCHA_PUBLIC_KEY']
    app.config['RECAPTCHA_PRIVATE_KEY'] = os.environ['RECAPTCHA_PRIVATE_KEY']

    enable_recaptcha = True
except KeyError:
    # Testing environment
    skey = token_bytes(16)
    enable_recaptcha = False

app.secret_key = skey

class TemplateSubmissionForm(FlaskForm):
    name = StringField('Your name', validators=[DataRequired(), Length(min=3)])
    email = StringField('Your email address', validators=[DataRequired()], render_kw={'type': 'email'})
    target_name = StringField('Recipient name', validators=[DataRequired(), Length(min=3)])
    target_email = StringField('Recipient email address', validators=[DataRequired()], render_kw={'type': 'email'})
    target_subject = StringField('Email subject', validators=[DataRequired()])
    target_body = TextAreaField('Email template', validators=[DataRequired()])
    if enable_recaptcha:
        recaptcha = RecaptchaField()

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

@app.route("/submit-template", methods=["GET", "POST"])
def submit_template():
    form = TemplateSubmissionForm()
    
    if request.method == "POST" and form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        target_name = form.target_name.data
        target_email = form.target_email.data
        target_subject = form.target_subject.data
        target_body = form.target_body.data

        # Do something with the inputs
        # createTemplate(...) --> emails.py:createTemplate(...)

        success = True

        if success:
            return redirect("/success")
    else:
        return render_template("submit-template.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/postcode/<postcode>")
def postcode(postcode):
    if validatePostcodeApi(postcode):
        return json.dumps(getAddresses(postcode))
    else:
        return make_response({"error": "Invalid postcode"}, 400)

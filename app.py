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
    abort
)
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from mpdetails import validate_postcode_api
from emailtemplates import (
    get_templates_by_topic,
    get_existing_templates,
    draft_templates,
)
from urllib import parse
from secrets import token_bytes
from address import get_addresses

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
    return render_template('404.html', error=error), 404

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
        empty_templates = get_existing_templates()
        emails = draft_templates(empty_templates, name, postcode, address)
        return render_template("all-topics.html", emails=emails)


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

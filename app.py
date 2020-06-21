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
from forms import TemplateSubmissionForm
from mpdetails import validate_postcode_api
from emailtemplates import (
    get_templates_by_topic,
    get_templates_by_slug,
    get_existing_templates,
    draft_templates,
    add_draft_template,
    EmailTemplate,
    TemplateSubmitter,
    UserBodySubmissionTemplate,
)
from database import myDb
from urllib import parse
from secrets import token_bytes
from address import get_addresses
from slugify import slugify

import emailtemplates
import json
import logging
import os
import sys

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

try:
    skey = bytes(os.environ["FLASK_SECRET_KEY"], "utf-8")

    app.config["RECAPTCHA_PUBLIC_KEY"] = os.environ["RECAPTCHA_PUBLIC_KEY"]
    app.config["RECAPTCHA_PRIVATE_KEY"] = os.environ["RECAPTCHA_PRIVATE_KEY"]

except KeyError:
    # Testing environment
    skey = token_bytes(16)
    # if testing is set to true, the RECAPTCHA field will always be valid
    # https://flask-wtf.readthedocs.io/en/stable/form.html#recaptcha
    app.testing = True
    app.config["RECAPTCHA_PUBLIC_KEY"] = skey
    app.config["RECAPTCHA_PRIVATE_KEY"] = skey


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
    return render_template("404.html", error=error), 404


class TemplateSubmissionForm(FlaskForm):
    name = StringField("Your name", validators=[DataRequired(), Length(min=3)])
    email = StringField(
        "Your email address", validators=[DataRequired()], render_kw={"type": "email"}
    )
    target_name = StringField(
        "Recipient name", validators=[DataRequired(), Length(min=3)]
    )
    target_email = StringField(
        "Recipient email address",
        validators=[DataRequired()],
        render_kw={"type": "email"},
    )
    target_subject = StringField("Email subject", validators=[DataRequired()])
    target_body = TextAreaField(
        "Email template", validators=[DataRequired()], render_kw={"rows": "10"}
    )
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
    new_template = EmailTemplate(**{"subject": "", "body": "", "name": ""})
    form = TemplateSubmissionForm()  # request.POST, obj=new_template

    if request.method == "POST" and form.validate_on_submit():
        # Get submitted body
        user_body = UserBodySubmissionTemplate(form.body.data)
        # Overwrite with converted body - ToDo: Check this is a legal operation
        form.body.data = user_body.convert_body()
        # Populate new_template object
        # ToDo: Check/handle behaviour of populate_obj on empty fields such as target, make sure pre-database storage validation can still take place
        form.populate_obj(new_template)

        try:
            # Validate and store draft template
            template_id = add_draft_template(new_template)
        except Exception:
            # ToDo: Handle template which have passed form validation but cannot be added
            # flash("Error when submitting template.", "danger")
            template_id = None
            success = False
            pass

        if template_id:
            submitter = TemplateSubmitter(
                name=form.submitter_name.data,
                email=form.submitter_email.data,
                template_id=template_id,
            )
            try:
                # success = add_submitter_info(submitter) # ToDo: Add submitter function
                success = True

            except Exception:
                success = False
                # ToDo: Handle incorrect storage of Submitter info
                pass
        if success:
            return redirect("/success")
        else:
            # ToDo: Handle failed template submission - error page?
            return

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

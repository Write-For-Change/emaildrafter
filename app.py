from flask import Flask, render_template, flash, jsonify, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from emails import draftEmails, validatePostcode
from urllib import parse

app = Flask(__name__)
app.secret_key = b'5bY4C!9R%aMHATv8rx0bUJB2'

class LandingForm(FlaskForm):
    fullname = StringField('Full Name', validators=[DataRequired(), Length(min=3)])
    postcode = StringField('Postcode', validators=[DataRequired(), validatePostcode])

@app.route("/", methods=["GET", "POST"])
def landing():
    form = LandingForm()

    if request.method == "GET":
        return render_template("landing.html", form=form)
    else:
        if form.validate_on_submit():
            name = form.fullname.data
            postcode = form.postcode.data.replace(" ", "")
            emails = None

            emails = draftEmails(name, postcode)

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
        else:
            return render_template("landing.html", form=form)


@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")
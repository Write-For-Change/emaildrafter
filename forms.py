"""
Submission form for EmailTemplates based on FlaskForms & wtforms

Written by:
Faizaan Pervaiz (fpervaiz)
David Swarbrick (davidswarbrick)
June 2020
"""

from flask_wtf import FlaskForm, RecaptchaField
from wtforms.fields import (
    StringField,
    SelectMultipleField,
    TextAreaField,
    SubmitField,
    BooleanField,
)
from wtforms.validators import DataRequired, Length, Email, ValidationError
from emailtemplates import UserBodySubmissionTemplate


def body_validator(form, field):
    if not UserBodySubmissionTemplate.check_submission_fields(field.data):
        raise ValidationError("Body contains illegal % escaped text")


class TemplateSubmissionForm(FlaskForm):
    submitter_name = StringField(
        "Your name", validators=[DataRequired(), Length(min=3)]
    )
    submitter_email = StringField(
        "Your email address",
        validators=[DataRequired(), Email()],
        render_kw={"type": "email"},
    )
    target_name = StringField(
        label="Recipient Name", description="Recipient name (Leave blank for Local MP)"
    )
    target_email = StringField(
        label="Recipient Email",
        description="Recipient email address (Leave blank for Local MP)",
        render_kw={"type": "email"},
    )
    author_url = StringField(
        label="Author URL",
        description="Link to the original template (if copied from elsewhere)",
    )
    more_info_url = StringField(
        label="More Info URL",
        description="URL for more information about this campaign",
    )
    name = StringField(
        label="Template Name",
        description="Short Description of Template (below 4 words if possible)",
    )
    subject = StringField("Email Subject", validators=[DataRequired(), Length(min=3)])
    body_description = "Fill out the template body here. The following shortcuts will be filled by our template system:\n{}\n\nFor example:\nDear %TONAME,\n\nMy name is %YOURNAME, I live at %YOURADDRESS in %CONSTITUENCY.\n Best wishes,\n %YOURNAME".format(
        UserBodySubmissionTemplate.get_allowed_fields()
    )
    body = TextAreaField(
        "Email Template",
        validators=[DataRequired(), body_validator],
        render_kw={"rows": "10"},
        description=body_description,
    )
    public = BooleanField(
        "Would you like this to be on the homepage? Your template will always be accessible from the relevant topic pages and via its unique URL."
    )
    recaptcha = RecaptchaField()

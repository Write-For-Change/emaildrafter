"""
Defining the Forms Django may use to parse data from a User and about a Template submission.
"""

from django import forms
from .models import EmailTemplate, EmailTemplateSubmitter


class UserForm(forms.Form):
    name = forms.CharField()
    postcode = forms.CharField()
    address = forms.CharField()
    email = forms.EmailField()


# As Template submissions and submitter info will be stored in a database we construct their forms from their model fields below
class TemplateSubmissionForm(forms.ModelForm):
    class Meta:
        model = EmailTemplate
        fields = [
            "name",
            "subject",
            "body",
            "more_info",
            "author_url",
            "target_is_local_mp",
            "public",
            "topics",
        ]


class TemplateSubmitterForm(forms.ModelForm):
    class Meta:
        model = EmailTemplateSubmitter
        fields = ["name", "email"]

from django import forms
from .models import EmailTemplate


class UserForm(forms.Form):
    name = forms.CharField()
    postcode = forms.CharField()
    address = forms.CharField()
    email = forms.EmailField()


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

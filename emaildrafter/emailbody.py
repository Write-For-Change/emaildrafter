"""
Functions relating to validating and filling template email bodies.

davidswarbrick 2020
"""
import re
from string import Template
from django.core.exceptions import ValidationError
from .forms import UserForm
from .models import EmailTarget


class EmailBody(Template):
    """Convert %TEMPLATEFIELD into the relevant information as appropriate, through inheriting the standard Python Template class"""

    delimiter = "%"
    # Turn off ignore case flag
    flags = 0
    # Detect capitals only, ending in non-word, whitespace, or end of string
    idpattern = r"([A-Z]+)(?=\W|\s|$)"

    ALLOWED_FIELDS = set(["YOURNAME", "YOURADDRESS", "TONAME", "CONSTITUENCY"])

    @staticmethod
    def construct_template_dict(user, target):
        """Construct a dictionary of substitutions from the input user and target objects"""
        assert isinstance(user, UserForm)
        # Check user form is valid
        assert user.is_valid()
        assert isinstance(target, EmailTarget)

        # This is currently decoupled from the ALLOWED_FIELDS class attribute, this may want to be addressed if extra allowed fields are added.
        # Ideally, a website administrator would be able to edit the replacement string and the attribute to which it is attached - this may require a different data model.
        template_dict = {
            # Use the cleaned data from the User submitted form
            "YOURNAME": user.cleaned_data["name"],
            "YOURADDRESS": user.cleaned_data["address"],
            "TONAME": target.name,
        }

        if hasattr(target, "constituency"):
            # Not all targets have a constituency
            template_dict["CONSTITUENCY"] = target.constituency

        return template_dict

    def fill(self, user, target):
        """Return a 'safe' substitution of all template fields to their values in template_dict.
        The 'safe' prefix means that invalid placeholders (following a % sign) will not raise errors, just pass through unchanged."""
        # ToDo : Validation on targets which will fit the template
        template_dict = EmailBody.construct_template_dict(user, target)
        return self.safe_substitute(**template_dict)

    @staticmethod
    def validate_body(body):
        """Checks if all %TEXT fields are in ALLOWED_FIELDS (i.e. they are allowed), raises a ValidationError if not"""
        f = re.compile(
            # Add the delimiter lookup at the start, but otherwise use the same settings as the Template substitute regex.
            r"(?<={})".format(EmailBody.delimiter) + EmailBody.idpattern,
            flags=EmailBody.flags,
        )
        fields_used = set(f.findall(body))
        # Check if all used fields exist in ALLOWED_FIELDS
        # Empty sets are included, as templates not using any submission fields are allowed
        if not fields_used <= EmailBody.ALLOWED_FIELDS:
            raise ValidationError("Illegal %FIELD in Email Body")

    @staticmethod
    def get_allowed_fields():
        return "".join("%{} ".format(k) for k in EmailBody.ALLOWED_FIELDS)

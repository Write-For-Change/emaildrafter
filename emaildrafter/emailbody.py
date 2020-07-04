"""
Functions relating to validating and filling template email bodies.

davidswarbrick 2020
"""
from string import Template


# ALLOWED_USER_FIELDS = set(["name", "address"])
# ALLOWED_TARGET_FIELDS = set(["name", "constituency", "email"])
# TEMPLATE_SUBMISSION_FIELDS = {
#     # %FIELD for input form to be replaced with dictionary lookup
#     # u = user dictionary, t = target dictionary
#     "YOURNAME": "{u[name]}",
#     "YOURADDRESS": "{u[address]}",
#     "CONSTITUENCY": "{t[constituency]}",
#     "TONAME": "{t[name]}",
# }


class UserBodySubmissionTemplate(Template):
    """Convert %TEMPLATEFIELD into the relevant information as appropriate, through inheriting the standard Python Template class"""

    delimiter = "%"
    # Turn off ignore case flag
    flags = 0
    # Detect capitals only, ending in non-word, whitespace, or end of string
    idpattern = r"([A-Z]+)(?=\W|\s|$)"

    # Dictionary

    def fill(self, **template_dict):
        """Return a 'safe' substitution of all template fields to their values in template_dict.
        The 'safe' prefix means that invalid placeholders (following a % sign) will not raise errors, just pass through unchanged."""
        return self.safe_substitute(**template_dict)

    # @staticmethod
    # def construct_template_dict(user,target):

    # @staticmethod
    # def check_submission_fields(body):
    #     """Returns True if all %TEXT fields are in TEMPLATE_SUBMISSION_FIELDS (i.e. they are allowed), returns False if not """
    #     f = re.compile(
    #         # Add the % lookup at the start, but otherwise use the same settings as the Template substitute regex.
    #         r"(?<=%)" + UserBodySubmissionTemplate.idpattern,
    #         flags=UserBodySubmissionTemplate.flags,
    #     )
    #     fields_used = set(f.findall(body))
    #     if fields_used <= set(TEMPLATE_SUBMISSION_FIELDS.keys()):
    #         # All fields exist in Template Submission Fields dict
    #         # Empty sets are included, as templates not using any submission fields are allowed
    #         return True
    #     else:
    #         return False
    #
    # @staticmethod
    # def get_allowed_fields():
    #     return "".join("%{} ".format(k) for k in TEMPLATE_SUBMISSION_FIELDS.keys())

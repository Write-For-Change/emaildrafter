"""
Object representation of EmailTemplates, plus functions to store and retrieve templates from the database.

Written by David Swarbrick (davidswarbrick) 2020
"""
import logging
import re
from database import myDb


# Instantiate the db connection:
mongo = myDb()

# Instantiate logging:
log = logging.getLogger("app")

ALLOWED_USER_FIELDS = ["name", "address"]
ALLOWED_TARGET_FIELDS = ["name", "constituency", "email"]


class EmailTemplate:
    """Object representation of email templates retrieved from database, providing construction from a dictionary, validation of inputs and template completion."""

    def __init__(self, **email_template_dict):
        # First, get the *required* aspects of the template,
        # and raise an error if these cannot be found
        try:
            self.subject = email_template_dict["subject"]
            self.body = self._parse_newlines_from_db(email_template_dict["body"])
            self.name = email_template_dict["name"]
        except KeyError:
            # If we cannot get a subject and body of the template it is unusable
            log.debug("Could not decode subject, body and used fields for the template")
            raise

        # If fields_used is already set, use those, otherwise generate new fields_used dict.
        try:
            self.fields_used = email_template_dict["fields_used"]
        except KeyError:
            self.fields_used = self._generate_used_fields(self.body)

        # Check this is a valid template
        self._validate_template_body(self.body, self.fields_used)

        # Attempt to get other details, and set default values if unavailable

        try:
            self.topics = email_template_dict["topics"]
        except KeyError:
            # An empty list of topics if none are stored
            self.topics = []

        try:
            self.more_info_url = email_template_dict["more_info_url"]
        except KeyError:
            self.more_info_url = None

        try:
            self.author_url = email_template_dict["author_url"]
        except KeyError:
            self.author_url = None

        try:
            self.cc = email_template_dict["cc"]
        except KeyError:
            self.cc = []

        try:
            self.target = email_template_dict["target"]

        except KeyError:
            # If target is None that means we are setting the target from MP data
            self.target = None

        # If a target is set, make sure it is valid
        if self.target:
            self._validate_target()

        try:
            self.public = email_template_dict["public"]
        except KeyError:
            self.public = False

        # Set the filled state to false
        self.filled = False

    @staticmethod
    def _parse_newlines_to_db(string_to_database):
        """Given a string, for example from a form input in HTML, replace newlines to prepare for storing the string in the database"""
        # Using a workaround discovered by Rafee (rafeeJ) temporarily
        return string_to_database.replace("\n", "\n")

    @staticmethod
    def _parse_newlines_from_db(string_from_database):
        """Given a string from the database, parse the newlines for correct display in HTML/emails etc."""
        # Empty for now, but could do some processing here
        return string_from_database

    @staticmethod
    def _generate_used_fields(template_body):
        """Generate the dictionary of the fields used in a specific template"""
        fields_used = {"target": [], "user": []}
        # Using regex to match "{t[]}" and "{u[]}"
        # (?<={t\[)\w+(?=\]}) -- positive look behind for {t[, match a word that ends with ]}
        target_searcher = re.compile(r"(?<={t\[)\w+(?=\]})")
        user_searcher = re.compile(r"(?<={u\[)\w+(?=\]})")
        # Use a set to make sure there is only one of each item, but return a list to the dictionary
        fields_used["target"] = list(set(target_searcher.findall(template_body)))
        fields_used["user"] = list(set(user_searcher.findall(template_body)))

        return fields_used

    @staticmethod
    def _validate_template_body(template_body, fields_used):
        """Check the template body matches the fields_used dictionary, and that all fields are legal choices."""

        # Generate the fields the template requires to check the supplied fields are correct
        template_fields_used = EmailTemplate._generate_used_fields(template_body)

        # Check the fields used in the template matches those we expect to be used:
        if set(fields_used["target"]) != set(template_fields_used["target"]):
            raise KeyError(
                "Supplied Target keys do not match Target fields in template"
            )
        if set(fields_used["user"]) != set(template_fields_used["user"]):
            raise KeyError("Supplied User keys do not match User fields in template")

        # Check the keys against the legal keys (set above)
        for key in fields_used["target"]:
            if key not in ALLOWED_TARGET_FIELDS:
                raise KeyError("Illegal Target Key Identified: {}".format(key))
        for key in fields_used["user"]:
            if key not in ALLOWED_USER_FIELDS:
                raise KeyError("Illegal User Key Identified: {}".format(key))

    def _validate_target(self):
        if self.target is None:
            raise AttributeError("Target not set for this template.")
        else:
            for key in self.fields_used["target"]:
                if key in self.target:
                    pass
                else:
                    raise KeyError("Template requires key not present in target info.")

    def _validate_user_info(self, user_info):
        for key in self.fields_used["user"]:
            if key in user_info:
                pass
            elif key == "address":
                # Handle people who don't give their address
                user_info["address"] = "[INPUT YOUR ADDRESS HERE]"
            else:
                raise KeyError("Template requires key not present in user info.")
        return user_info

    def __str__(self):
        return str([self.subject, self.body])

    def set_target(self, name, email, constituency=None):
        self.target = {
            "name": name,
            "email": email,
            "constituency": constituency,
        }

    def fill(self, user_info):
        """Fill an unfilled body with provided user information (user_info)"""
        if self.filled:
            # Already filled, so do not need to fill again
            return self.filled
        self._validate_target()
        validated_user_info = self._validate_user_info(user_info)
        self.body = self.body.format(t=self.target, u=validated_user_info)
        self.filled = True
        return self.filled


def get_existing_templates(query=None, only_public=True):
    """Grab all the template options that exist so far"""

    # Returns an array of JSON objects from the email_templates collection.
    if query is None:
        # Default is get all of the email templates
        emails = mongo.get_all("email_templates")
    else:
        # However if a query is specified, only return templates matching the query
        emails = mongo.get_all_matching("email_templates", query)

    templates = []
    for e in emails:
        # Iterate through emails and create EmailTemplate objects
        if only_public:
            if e["public"]:
                # Only append public templates
                templates.append(EmailTemplate(**e))
        else:
            templates.append(EmailTemplate(**e))

    return templates


def pre_database_template_validation(**template_dict):
    """Check the template dictionary is valid before sending to database"""
    try:
        et = EmailTemplate(**template_dict)

    except KeyError as k:
        log.debug("Template invalid: ", k)
        raise
    return template_dict


def add_or_update_template(**t):
    # Check if template using this name already exists, and update if so.
    template_dict = pre_database_template_validation(t)
    existing_template = mongo.get_one(
        "email_templates", {"name": template_dict["name"]}
    )
    if existing_template:
        # Update existing template
        mongo.update_one(
            "email_templates", {"name": template_dict["name"]}, template_dict
        )
        return True
    else:
        # Template doesn't exist so create this template
        mongo.insert_one("email_templates", template_dict)
        return True

"""
Object representation of EmailTemplates, plus functions to store and retrieve templates from the database.

Written by David Swarbrick (davidswarbrick) 2020
"""
from database import myDb
import logging


# Instantiate the db connection:
mongo = myDb()

# Instantiate logging:
log = logging.getLogger("app")


class EmailTemplate:
    """Object representation of email templates retrieved from database, providing construction from a dictionary, validation of inputs and template completion."""

    def __init__(self, **email_template_dict):
        # First, get the *required* aspects of the template,
        # and raise an error if these cannot be found
        try:
            self.subject = email_template_dict["subject"]
            self.body = self._parse_newlines_from_db(email_template_dict["body"])
            self.name = email_template_dict["name"]
            self.fields_used = email_template_dict["fields_used"]
        except KeyError:
            # If we cannot get a subject and body of the template it is unusable
            log.debug("Could not decode subject, body and used fields for the template")
            raise

        # Second, attempt to get other details, and set default values if unavailable

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
        # To be implemented - most likely using regex to match "{t[]}" and "{u[]}"
        return fields_used

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


# Reference dictionaries for user and target info
user_info = {
    "name": "John Smith",
    "address": "1 Test Road, Somewhere, AB1 2CD",
}
target_info = {
    "name": "Big Bad Government",
    "constituency": "Westminster",
    "email": "bigbadboi@hotmail.co.uk",
}

# This dictionary represents how a template will be stored in the database
example_template = {
    # Subject field: To be entered in the subject field of mailto and gmail links
    "subject": "Justice for an Email Template Example",
    # Body field: Content of the template including dictionary lookups for auto-filling later
    "body": "dear {t[name]},\nLots of complex ideas and thoughts\n expressed well (handle newlines) from: {u[name]} {u[address]}",
    # Name of the template: ideally 3-4 words max to allow a quick description of this template, may be the same as the subject line of the email for some templates.
    # This will be used to check if template already exists so AVOID RENAMING TEMPLATES
    "name": "Three-Four Word description",
    # List of topics that this email tackles,
    # This will allow filtering templates by topic at a general level (eg "All Templates on Racial Injustice") and on a more specific level (eg "Belly Mujinga")
    "topics": ["Wide, overarching issue", "Specific topic of this template"],
    # URL linking to the author of the template: "This template was written by [This Person]("template_author_url")"
    "author_url": "https://twitter.com/ACoolGuy/status/emailtemplateidea",
    # URL linking to more information on this campaign: "More info for this campaign can be found [here]("template_more_info_url")"
    "more_info_url": "https://campaign-website.com",
    # The target the template is addressed to.
    # The "target" field is only set if the target for the email is known before getting user data, i.e. always the same person.
    # If the "target" field is unset, the target relies on user input, and thus we assume the target must be the local MP of the website user.
    # In the future we may want to store targets separately, however for now we store their information as a dictionary under the target field of the template.
    "target": {
        # "Name" and "Email" are the only required fields for targets at the moment, however in the future more complex templates may require attributes such as "department"
        "name": "CEO of Bad Company",
        "email": "ceo@company.com",
    },
    # CC- carbon copy addresses: A list of emails to put in the cc field of the email, we may want to extend this later, for example to include LOCALMP or some other flag to allow an MP to be copied into an email to a head of a government department.
    "cc": ["anotherperson@company.com"],
    # The attributes of the user and target dictionaries which the body of the template requires to be filled correctly.
    # Used for validation of the template against provided user & target info
    "fields_used": {"target": ["name"], "user": ["name", "address"],},
    # Flag setting template visibility
    # Later when private campaigns are implemented we won't want to serve every template on the homepage - this flag allows us to disable templates without deleting them.
    "public": True,
}


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

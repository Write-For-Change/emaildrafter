import unittest
from copy import deepcopy
from emailtemplates import EmailTemplate

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


class TestEmailTemplate(unittest.TestCase):
    def setUp(self):
        self.template_dict = example_template

    def test_missing_attributes(self):
        """Tests to check EmailTemplate object creation fails as expected when template_dict is missing attributes"""
        # Want essential components of a template to generate key errors:
        for a in ["subject", "body", "name"]:
            # Make a copy of the example dictionary
            dict = deepcopy(self.template_dict)
            with self.subTest(a=a):
                # Delete the "a" field
                del dict[a]
                with self.assertRaises(KeyError):
                    et = EmailTemplate(**dict)
        # Unnecessary attributes should be able to be missing and still create a valid template
        for b in [
            "topics",
            "author_url",
            "more_info_url",
            "target",
            "cc",
            "fields_used",
            "public",
        ]:
            dict = deepcopy(self.template_dict)
            with self.subTest(b=b):
                # Delete the "b" field
                del dict[b]
                # Email Template generation should succeed successfully
                et = EmailTemplate(**dict)

    def test_generate_user_fields(self):
        """
        Tests the correct user fields are generated from a template body:
        - Each field should only be extracted once (no duplicates)
        - Attributes should be a single word
        - The syntax for a field is strictly {t[attribute]} or {u[attribute]} (no newlines or missed brackets)
        """
        body = "dear {t[name]},\n I am  {u[name]} ... u[name] {uname} u[{] [{name_no_u}] {u[nameacrosslines]\n}  {u[name]} {u[address]}"
        expected_fields = {"user": ["name", "address"], "target": ["name"]}
        self.assertCountEqual(
            EmailTemplate._generate_used_fields(body), expected_fields
        )

    def test_invalid_attributes_in_template(self):
        """Tests that if there are invalid attributes in the body, the template fails"""
        dict = deepcopy(self.template_dict)
        dict["body"] = "Dear {t[names]}, {u[name]}"
        with self.assertRaises(KeyError):
            et = EmailTemplate(**dict)


if __name__ == "__main__":
    unittest.main()

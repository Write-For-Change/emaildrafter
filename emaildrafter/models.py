"""
Data models used elsewhere in the EmailDrafter application.
Used by Django to construct relevant tables in the database, to ease form creation in HTML and to standardise any other interactions with this data.

David Swarbrick (davidswarbrick) 2020
"""
from django.db import models
from django.urls import reverse
from urllib.parse import quote
from .emailbody import EmailBody
from .externalapis import get_constituency


class EmailTemplate(models.Model):
    """Model for Email Templates as stored in the database."""

    # https://stackoverflow.com/questions/1592291/what-is-the-email-subject-length-limit
    subject = models.CharField(max_length=78)
    body = models.TextField(validators=[EmailBody.validate_body])
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    # blank = True allows these extra information fields to be empty
    more_info = models.URLField(blank=True)
    author_url = models.URLField(blank=True)
    target_is_local_mp = models.BooleanField(default=True)
    public = models.BooleanField(default=False)
    admin_approved = models.BooleanField(default=False)
    upload_date = models.DateTimeField()

    # Target field only set if NOT target_is_local_mp, stores a related target object
    target = models.OneToOneField(
        "SpecificTarget", on_delete=models.CASCADE, default=None, blank=True
    )
    # Multiple topics can be associated with a template
    topics = models.ManyToManyField("Topic", blank=True)

    # Template filling & display

    filled_body = ""
    filled = False

    def fill(self, user_form):
        """Fill the empty template body, getting MP information if no target is set"""
        # Construct an EmailBody template object
        empty_body = EmailBody(self.body)

        if self.target is None:
            # If target has not been set, then it should be replaced with a user's MP
            # Get the relevant MP using the constituency from the form the user submitted.
            mp = MP.objects.get(constituency=user_form.clean_data["constituency"])
            # Set this mp as the target of this template
            # NB do not call .save() on this object as we do not wish this change to persist beyond a single user.
            self.target = mp

        self.filled_body = empty_body.fill(user_form, self.target)
        self.filled = True

    def get_absolute_url(self):
        """Set the url for each template to use the slug field."""
        return reverse("single-template", kwargs={"slug": self.slug})

    @property
    def mailto_subject(self):
        """Passes the subject through the urllib quote parser for usage in mailto links in HTML"""
        return quote(self.subject)

    @property
    def mailto_filled_body(self):
        """Passes the body through the urllib quote parser for usage in mailto links in HTML"""
        return quote(self.filled_body).replace("%0A", "%0D%0A")


class EmailTarget(models.Model):
    """Abstract base class for email targets with their common required information"""

    name = models.CharField(max_length=200)
    email = models.EmailField()

    class Meta:
        abstract = True


class MP(EmailTarget):
    """Class for MPs to store their specific information required by templates."""

    constituency = models.CharField(max_length=200)
    party = models.CharField(max_length=200)


class SpecificTarget(EmailTarget):
    """Class for a singular target for an email template, currently empty as no information beyond the abstract EmailTarget class is required, however this class is needed as abstract base classes are not managed by Django."""

    pass


class Topic(models.Model):
    """Store the Topics of the templates separately"""

    name = models.CharField(max_length=200)
    slug = models.SlugField()
    more_info = models.URLField()
    description = models.TextField()


class EmailTemplateSubmitter(models.Model):
    """A user of the site who submits a template or topic."""

    name = models.CharField(max_length=254)
    email = models.EmailField()
    # Store the template this user has submitted. On deletion of the template, delete the user's information also.
    template = models.OneToOneField(EmailTemplate, on_delete=models.CASCADE)

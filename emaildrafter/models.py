from django.db import models


class EmailTemplate(models.Model):
    """Model for Email Templates as stored in the database."""

    # https://stackoverflow.com/questions/1592291/what-is-the-email-subject-length-limit
    subject = models.CharField(max_length=78)
    body = models.TextField()
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    # blank = True allows these extra information fields to be empty
    more_info = models.URLField(blank=True)
    author_url = models.URLField(blank=True)
    target_is_local_mp = models.BooleanField(default=True)
    public = models.BooleanField(default=False)
    upload_date = models.DateTimeField()

    # Target field only set if NOT target_is_local_mp, stores a related target object
    target = models.OneToOneField(
        "SpecificTarget", on_delete=models.CASCADE, default=None
    )
    # Multiple topics can be associated with a template
    topics = models.ManyToManyField("Topic")


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

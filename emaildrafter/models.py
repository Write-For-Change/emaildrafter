from django.db import models


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


class EmailTemplate(models.Model):
    """Model for Email Templates as stored in the database."""

    # https://stackoverflow.com/questions/1592291/what-is-the-email-subject-length-limit
    subject = models.CharField(max_length=78)
    body = models.TextField()
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    # Want to have a link to a Target object, but need to discuss how to store this ie many-to-one/one-to-one etc.
    # Will take a form similar to below: (this fails as EmailTarget is abstract)
    # target = models.ForeignKey(EmailTarget, on_delete=models.CASCADE,)


class EmailTemplateSubmitter(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField()

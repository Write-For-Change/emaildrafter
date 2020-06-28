from django.db import models


class EmailTemplate(models.Model):
    # https://stackoverflow.com/questions/1592291/what-is-the-email-subject-length-limit
    subject = CharField(max_length=78)
    body = TextField()

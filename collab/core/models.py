from django.db import models


class Document(models.Model):
    body = models.TextField()

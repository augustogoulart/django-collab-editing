from django.db import models


class Document(models.Model):
    body = models.TextField()
    serialized_selection = models.CharField(max_length=255, null=True)


from django.db import models


class Document(models.Model):
    body = models.TextField()


class Selection(models.Model):
    document = models.ForeignKey('Document', on_delete=models.CASCADE)
    selection = models.CharField(max_length=255, null=True)

from django import forms
from collab.core.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['body']


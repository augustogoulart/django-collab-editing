from django import forms
from collab.core.models import Document, Selection


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['body']


class SelectionForm(forms.ModelForm):
    class Meta:
        model = Selection
        fields = ['selection', 'document']

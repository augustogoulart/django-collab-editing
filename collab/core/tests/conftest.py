import pytest

from collab.core.models import Document, Selection


@pytest.fixture()
def selection(document):
    return Selection.objects.create(document=document)


@pytest.fixture()
def document(db):
    return Document.objects.create(body='body')

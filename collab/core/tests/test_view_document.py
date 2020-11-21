import pytest

from collab.core.models import Document, Selection
from pytest_django.asserts import assertTemplateUsed


def test_document_get(document, client):
    resp = client.get('/document/')
    assert resp.status_code == 200


@pytest.mark.skip()
def test_document_post(document, client):
    resp = client.post('/document/')
    assert resp.status_code == 200


@pytest.mark.skip()
def test_update_document(document, client):
    resp = client.post('/document/')


def test_assert_template_used(document, client):
    resp = client.get('/document/')
    assertTemplateUsed(resp, 'core/document.html')


def test_document_view_context(document, client):
    resp = client.get('/document/')
    assert "document" in resp.context


def test_document_context_fields_get(document, client):
    resp = client.get('/document/')
    document = resp.context['document']
    assert "body" in document

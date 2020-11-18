from collab.core.models import Document
from pytest_django.asserts import assertTemplateUsed


def test_document_get(db, client):
    resp = client.get('/document/')
    assert resp.status_code == 200


def test_document_post(db, client):
    resp = client.post('/document/')
    assert resp.status_code == 200


def test_update_document(db, client):
    resp = client.post('/document/')

def test_assert_template_used(db, client):
    resp = client.get('/document/')
    assertTemplateUsed(resp, 'core/document.html')


def test_document_view_context(db, client):
    resp = client.get('/document/')
    assert "document" in resp.context


def test_document_context_fields(db, client):
    Document.objects.create(body="body")
    resp = client.get('/document/')
    document = resp.context['document']
    assert "body" in document
    assert "serialized_selection" in document

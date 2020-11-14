from pytest_django.asserts import assertTemplateUsed


def test_document_get(client):
    resp = client.get('/document/')
    assert resp.status_code == 200


def test_assert_template_used(client):
    resp = client.get('/document/')
    assertTemplateUsed(resp, 'core/document.html')

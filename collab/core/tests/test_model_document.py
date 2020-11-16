from collab.core.models import Document


def test_can_create_document(db):
    Document.objects.create()
    assert Document.objects.exists()

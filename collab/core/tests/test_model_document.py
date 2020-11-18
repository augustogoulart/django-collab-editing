from collab.core.models import Document


def test_can_create_document(db):
    Document.objects.create()
    assert Document.objects.exists()


def test_serialized_selection_can_be_blank(db):
    document = Document.objects.create(body='body')
    assert document.serialized_selection is None

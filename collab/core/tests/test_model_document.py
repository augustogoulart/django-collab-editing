from collab.core.models import Document, Selection


def test_can_create_document(document):
    assert Document.objects.exists()


def test_document_can_have_multiple_selections(document):
    Selection.objects.create(selection="0/6/0/2/1/2:199,0/6/0/2/1/2:327", document=document)
    Selection.objects.create(selection="0/2/0/2/1/2:700,0/4/0/2/1/2:220", document=document)
    assert document.selection_set.count() == 2

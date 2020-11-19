from collab.core.models import Document, Selection


def test_serialized_selection_can_be_blank(db):
    document = Document.objects.create(body='body')
    selection = Selection.objects.create(document=document)
    assert selection.selection is None

from collab.core.forms import DocumentForm


def test_validate():
    data = dict(
        body="<p>document body</p>",
        serialized_selection="0/2/0/2/1/2:7,0/2/0/2/1/2:295{75cb7623}"
    )
    form = DocumentForm(data)
    form.is_valid()
    assert form.cleaned_data['body']
    assert form.cleaned_data['serialized_selection']

from collab.core.forms import DocumentForm


def test_validate():
    data = dict(
        body="<p>document body</p>"
    )
    form = DocumentForm(data)
    form.is_valid()
    assert form.cleaned_data['body']

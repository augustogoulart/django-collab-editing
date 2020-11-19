from collab.core.forms import SelectionForm


def test_validate():
    data = dict(
        selection="0/6/0/2/1/2:199,0/6/0/2/1/2:327"
    )
    form = SelectionForm(data)
    form.is_valid()
    assert form.cleaned_data['selection']

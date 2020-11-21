from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from collab.core.forms import DocumentForm, SelectionForm
from collab.core.models import Document


@csrf_exempt
def document(request):
    document = Document.objects.all()
    if request.method == 'POST':
        form = SelectionForm(
            {"selection": request.POST['selection'],
             "document": document.first()
             }
        )
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return HttpResponse()

    try:
        selection_set = document.first().selection_set.all()
    except AttributeError:
        selection_set = {}

    return render(request, 'core/document.html', {
        'document': serialize('json', document),
        'selections': serialize('json', selection_set)
    })

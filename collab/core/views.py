from django.shortcuts import render
from collab.core.models import Document
from collab.core.forms import DocumentForm
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize


@csrf_exempt
def document(request):
    documents = Document.objects.all()
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=documents.first())
        if form.is_valid():
            form.save()
    return render(request, 'core/document.html', {'document': serialize('json', documents)})

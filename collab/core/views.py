from django.shortcuts import render
from collab.core.models import Document
from collab.core.forms import DocumentForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def document(request):
    document = Document.objects.all().first()
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
    return render(request, 'core/document.html', {'document': document})

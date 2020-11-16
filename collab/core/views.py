from django.shortcuts import render
from collab.core.models import Document


def document(request):
    return render(request, 'core/document.html', {'document': Document.objects.all().first()})

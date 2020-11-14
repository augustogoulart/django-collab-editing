from django.shortcuts import render


def document(request):
    return render(request, 'core/document.html')

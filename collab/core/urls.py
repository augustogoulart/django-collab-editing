from django.urls import path
from collab.core.views import document


urlpatterns = [
    path('', document)
]

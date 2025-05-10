from django.urls import path
from api.view.source.views import content_respo

urlpatterns = [
    path('data/', content_respo),
]

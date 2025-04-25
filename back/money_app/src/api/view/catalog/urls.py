from django.urls import path
from api.view.catalog.views import content_respo

urlpatterns = [
    path('table/', content_respo),
]

from django.urls import path
from api.view.v1.views import content_respo


urlpatterns = [
    path('task/', content_respo),
]

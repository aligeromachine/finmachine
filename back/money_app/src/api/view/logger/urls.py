from django.urls import path
from api.view.logger.views import content_respo

urlpatterns = [
    path('data/', content_respo),
]

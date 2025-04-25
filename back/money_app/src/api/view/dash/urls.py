from django.urls import path
from api.view.dash.views import content_respo

urlpatterns = [
    path('update/', content_respo),
]

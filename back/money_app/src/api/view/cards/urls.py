from django.urls import path
from api.view.cards.views import content_respo

urlpatterns = [
    path('table/', content_respo),
]

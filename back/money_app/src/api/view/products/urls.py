from django.urls import path
from api.view.products.views import content_respo

urlpatterns = [
    path('data/', content_respo),
]

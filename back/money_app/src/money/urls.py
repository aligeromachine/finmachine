from django.urls import path, include


urlpatterns = [
    path(route='', view=include('money.view.urls')),
]

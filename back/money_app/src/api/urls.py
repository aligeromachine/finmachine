from django.urls import path, include


urlpatterns = [
    path(route='api/', view=include('api.view.urls')),
]

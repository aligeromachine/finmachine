from django.urls import path, include


urlpatterns = [
    path(route='v1/', view=include('api.view.v1.urls')),
    path(route='v1/', view=include('api.view.v1.func.urls')),
]

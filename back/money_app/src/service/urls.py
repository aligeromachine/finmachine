from django.urls import path, include, re_path
from django.views.static import serve
from service.settings import MEDIA_ROOT, STATIC_ROOT

urlpatterns = [

    path('', include('authentication.urls')),
    path('', include('money.urls')),
    path('', include('api.urls')),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),

]

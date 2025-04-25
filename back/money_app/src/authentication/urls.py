from django.urls import path
from authentication.views import custom_logout, login_view, protected_view, refresh_token_view, register_view

urlpatterns = [
    path('api/auth/login/', login_view, name='login'),
    path('api/auth/refresh/', refresh_token_view, name='refresh_token'),
    path('api/auth/protected/', protected_view, name='protected'),
    path('api/auth/logout/', custom_logout, name='logout'),
    path('api/auth/register/', register_view, name='logout'),
]

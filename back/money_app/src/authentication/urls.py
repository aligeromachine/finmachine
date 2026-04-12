from django.urls import path
from authentication.views import custom_logout, login_view, protected_view, refresh_token_view, register_view

urlpatterns = [
    path(route='api/auth/login/', view=login_view),
    path(route='api/auth/refresh/', view=refresh_token_view),
    path(route='api/auth/protected/', view=protected_view),
    path(route='api/auth/logout/', view=custom_logout),
    path(route='api/auth/register/', view=register_view),
]

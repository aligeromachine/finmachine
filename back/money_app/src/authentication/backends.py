# backends.py
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from authentication.utils import verify_jwt_token

User = get_user_model()

class JWTAuthenticationBackend:
    def authenticate(self, request: HttpRequest, token: str = None):
        if token is None:
            return None

        payload, _ = verify_jwt_token(token)
        if not payload:
            return None

        try:
            user = User.objects.get(pk=payload['user_id'])
            return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

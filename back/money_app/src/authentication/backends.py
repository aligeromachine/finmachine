# backends.py
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from authentication.utils import verify_jwt_token
import logging

logger = logging.getLogger(__name__)

User = get_user_model()

class JWTAuthenticationBackend:
    def authenticate(self, request: HttpRequest, token: str = '') -> AbstractUser | None:
        if not token:
            return None

        logger.info(token)
        payload, _ = verify_jwt_token(token)
        if not payload:
            return None

        try:
            user = User.objects.get(pk=payload['user_id'])
            return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id: int) -> AbstractUser | None:
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

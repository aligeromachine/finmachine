from django.contrib.auth import get_user_model
from authentication.config import ACCESS_LIFETIME, REFRESH_LIFETIME, ALGORITHM, SECRET_KEY
import jwt
from datetime import datetime, timezone

def create_jwt_tokens(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        # Генерация токенов
        access_payload = {
            'user_id': instance.id,
            'type': 'access',
            'exp': datetime.now(timezone.utc) + ACCESS_LIFETIME,
            'iat': datetime.now(timezone.utc)
        }

        refresh_payload = {
            'user_id': instance.id,
            'type': 'refresh',
            'exp': datetime.now(timezone.utc) + REFRESH_LIFETIME,
            'iat': datetime.now(timezone.utc)
        }

        access_token = jwt.encode(
            access_payload,
            SECRET_KEY,
            algorithm=ALGORITHM
        )

        refresh_token = jwt.encode(
            refresh_payload,
            SECRET_KEY,
            algorithm=ALGORITHM
        )
        print(f'JWT Tokens for superuser {instance.username}:')
        print(f'Access Token: {access_token}')
        print(f'Refresh Token: {refresh_token}')

def register_handlers():
    from django.db.models.signals import post_save
    post_save.connect(create_jwt_tokens, sender=get_user_model())

from django.contrib.auth import get_user_model
from typing import Any
from authentication.utils import create_jwt_tokens

def create_jwt(sender: Any, instance: Any, created: bool, **kwargs: Any) -> None:
    if created and instance.is_superuser:
        # Генерация токенов
        tokens = create_jwt_tokens(instance.id)

        print(f'JWT Tokens for superuser {instance.username}:')
        print(f'Access Token: {tokens['access']}')
        print(f'Refresh Token: {tokens['refresh']}')

def register_handlers() -> None:
    from django.db.models.signals import post_save
    post_save.connect(create_jwt, sender=get_user_model())

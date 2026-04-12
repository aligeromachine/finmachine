import jwt
from datetime import datetime, timezone, timedelta
from authentication.config import ACCESS_LIFETIME, REFRESH_LIFETIME, ALGORITHM, SECRET_KEY
from typing import Callable
import logging

logger = logging.getLogger(__name__)


encode: Callable[[dict], str] = lambda token: jwt.encode(payload=token, key=SECRET_KEY, algorithm=ALGORITHM)
decode: Callable[[str], dict] = lambda token: jwt.decode(jwt=token, key=SECRET_KEY, algorithms=ALGORITHM)

def create_token(user_id: int, minutes: int = 0, days: int = 0) -> dict:
    return dict(
        user_id=user_id,
        exp=datetime.now(timezone.utc) + timedelta(days=days, minutes=minutes),
        iat=datetime.now(timezone.utc)
    )

def create_jwt_tokens(user_id: int) -> dict:
    access = create_token(user_id=user_id, minutes=ACCESS_LIFETIME)
    refresh = create_token(user_id=user_id, days=REFRESH_LIFETIME)
    return dict(access=encode(access), refresh=encode(refresh))

def verify_jwt_token(token: str) -> tuple:
    payload: dict | None = None
    err: str | None = None

    try:
        payload = decode(token)
    except jwt.ExpiredSignatureError:
        err = "Token expired"
    except jwt.InvalidTokenError as e:
        err = f"Invalid token: {str(e)}"
    except Exception as e:
        err = f"Decoding error: {str(e)}"

    return payload, err

def get_token_info(token: str) -> dict:
    """
    Получение информации о JWT токене
    """
    try:
        # Декодируем токен без проверки подписи для получения информации
        # Важно: используем тот же секретный ключ, что и для подписи
        decoded_token = decode(token)

        # Получаем время истечения из payload
        exp_timestamp = decoded_token.get('exp')
        if exp_timestamp:
            exp_datetime = datetime.fromtimestamp(exp_timestamp)
            current_datetime = datetime.now()
            time_left = exp_datetime - current_datetime

            return dict(
                user_id=decoded_token.get('user_id'),
                expires_at=exp_datetime.strftime('%Y-%m-%d %H:%M:%S'),
                minutes=round(time_left.total_seconds() / 60, 2),
                hours=round(time_left.total_seconds() / 3600, 2),
                is_expired=time_left.total_seconds() <= 0,
            )
        else:
            return {'error': 'Токен не содержит поле exp'}

    except jwt.InvalidSignatureError:
        return {'error': 'Неверная подпись токена'}
    except jwt.DecodeError:
        return {'error': 'Ошибка декодирования токена'}
    except Exception as e:
        return {'error': f'Ошибка при обработке токена: {str(e)}'}

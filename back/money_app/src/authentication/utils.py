import jwt
from datetime import datetime, timezone, timedelta
from authentication.config import ACCESS_LIFETIME, REFRESH_LIFETIME, ALGORITHM, SECRET_KEY
from typing import Callable
import logging

encode: Callable = lambda token: jwt.encode(payload=token, key=SECRET_KEY, algorithm=ALGORITHM)
decode: Callable = lambda token: jwt.decode(jwt=token, key=SECRET_KEY, algorithms=ALGORITHM)

logger = logging.getLogger(__name__)

def create_jwt_tokens(user_id: int) -> dict:
    access_payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_LIFETIME),
        "iat": datetime.now(timezone.utc)
    }

    refresh_payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(days=REFRESH_LIFETIME),
        "iat": datetime.now(timezone.utc)
    }

    return {
        "access": encode(access_payload),
        "refresh": encode(refresh_payload)
    }

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

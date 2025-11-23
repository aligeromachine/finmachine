import jwt
from datetime import datetime, timezone, timedelta
from authentication.config import ACCESS_LIFETIME, REFRESH_LIFETIME, ALGORITHM, SECRET_KEY
from typing import Callable
import logging

logger = logging.getLogger(__name__)


encode: Callable[[dict], str] = lambda token: jwt.encode(payload=token, key=SECRET_KEY, algorithm=ALGORITHM)
decode: Callable[[str], dict] = lambda token: jwt.decode(jwt=token, key=SECRET_KEY, algorithms=ALGORITHM)

def create_token(user_id: int, life: int) -> dict:
    return dict(
        user_id=user_id,
        exp=datetime.now(timezone.utc) + timedelta(minutes=life),
        iat=datetime.now(timezone.utc)
    )

def create_jwt_tokens(user_id: int) -> dict:
    access = create_token(user_id=user_id, life=ACCESS_LIFETIME)
    refresh = create_token(user_id=user_id, life=REFRESH_LIFETIME)
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

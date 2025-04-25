import jwt
from datetime import datetime, timezone
from authentication.config import ACCESS_LIFETIME, REFRESH_LIFETIME, ALGORITHM, SECRET_KEY

def create_jwt_tokens(user_id: int):
    access_payload = {
        'user_id': user_id,
        'type': 'access',
        'exp': datetime.now(timezone.utc) + ACCESS_LIFETIME,
        'iat': datetime.now(timezone.utc)
    }

    refresh_payload = {
        'user_id': user_id,
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

    return {
        'access': access_token,
        'refresh': refresh_token
    }

def verify_jwt_token(token: str):
    payload: dict = None
    err: str = None
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )        
    except jwt.ExpiredSignatureError:
        err = 'Invalid token'
    except jwt.InvalidTokenError:
        err = 'Token expired'

    return payload, err

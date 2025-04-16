from functools import wraps
from typing import Callable
from django.http import HttpRequest, JsonResponse
import jwt
from datetime import datetime, timezone
from pydantic import BaseModel
from authentication.model import validate_dict
from service.settings import (
    JWT_ACCESS_TOKEN_LIFETIME, 
    JWT_REFRESH_TOKEN_LIFETIME, 
    JWT_SECRET_KEY, 
    JWT_ALGORITHM)

def create_jwt_tokens(user_id: int):
    access_payload = {
        'user_id': user_id,
        'type': 'access',
        'exp': datetime.now(timezone.utc) + JWT_ACCESS_TOKEN_LIFETIME,
        'iat': datetime.now(timezone.utc)
    }

    refresh_payload = {
        'user_id': user_id,
        'type': 'refresh',
        'exp': datetime.now(timezone.utc) + JWT_REFRESH_TOKEN_LIFETIME,
        'iat': datetime.now(timezone.utc)
    }
    
    access_token = jwt.encode(
        access_payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM
    )
    
    refresh_token = jwt.encode(
        refresh_payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM
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
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )        
    except jwt.ExpiredSignatureError:
        err = 'Invalid token'
    except jwt.InvalidTokenError:
        err = 'Token expired'

    return payload, err

def token_response(token: dict = None, msg: str = None, code: int = 200):
    return JsonResponse({'token': token, 'message': msg}, status=code)

def check_post(view_func):
    def wrapper_view(request: HttpRequest):
        
        if request.method != 'POST':
            return token_response(msg='Method not allowed', code=405)
        
        return view_func(request)
    return wrapper_view

def parse_auth(Model: type[BaseModel]):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(request: HttpRequest, *args, **kwargs):
            
            data: BaseModel = validate_dict(response=request.body, Model=Model)
            if not data:
                return token_response(msg='Invalid data Model', code=400)
    
            return func(request, data, *args, **kwargs)
        return wrapper
    return decorator

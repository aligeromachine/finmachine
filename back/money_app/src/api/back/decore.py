from collections.abc import Callable
from functools import wraps
import logging
from typing import TypeVar, Any
from pydantic import BaseModel
from django.http import HttpRequest
from money.libs.validate import validate_dict_conv

R = TypeVar("R")
logger = logging.getLogger(__name__)

class MainModel(BaseModel):
    user_id: int = 0
    command: str

class FData(BaseModel):
    b64: str
    name: str
    type: str

class ExtModel(MainModel):
    offset: int = 0
    limit: int = 0
    pk: int = 0
    title: str = ''

def draw_paginate(func: Callable[..., dict]) -> Callable[..., dict]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> dict:
        ls, count, offset, limit = func(*args, **kwargs)
        result: dict = {
            'recordsTotal': count,
            'offset': offset,
            'recordsDisplay': limit,
            'draw': ls
        }
        return result
    return wrapper

def validate_model(Model: type[MainModel]) -> Callable[..., Callable[..., dict]]:
    def decorator(func: Callable[..., dict]) -> Callable[..., dict]:
        @wraps(func)
        def wrapper(request: HttpRequest, *args: Any, **kwargs: Any) -> dict:

            data: MainModel = validate_dict_conv(request.body, Model=Model)
            if not data:
                return {'data': 'err', 'message': f'validate_dict_conv: {Model}'}

            data.user_id = request.user_id
            return func(request, data, *args, **kwargs)
        return wrapper
    return decorator

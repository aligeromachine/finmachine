from collections.abc import Callable
from datetime import datetime, timedelta
from functools import wraps
import logging
from typing import Self, TypeVar, Any
from pydantic import BaseModel, model_validator
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
    created: str | datetime = datetime.now() + timedelta(hours=3)

    @model_validator(mode='after')
    def complete(self) -> Self:
        if isinstance(self.created, str) and self.created:
            dt: datetime | None = None
            fmt_iso: str = "%Y-%m-%dT%H:%M:%S"
            fmt_js: str = "%a %b %d %Y %H:%M:%S"
            if not dt:
                try:
                    dt = datetime.strptime(self.created, "%Y-%m-%dT%H:%M:%S")
                except ValueError as ex:
                    pass
            
            if not dt:
                try:
                    dt = datetime.strptime(self.created, "%a %b %d %Y %H:%M:%S")
                except ValueError:
                    pass

            if not dt:
                raise Exception(f"{self.created} does not match with {fmt_iso}, {fmt_js}")
            
            self.created = dt
        return self

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

            data: MainModel = validate_dict_conv(request.body, Model=Model, prn=True)
            if not data:
                return {'data': 'err', 'message': f'validate_dict_conv: {Model}'}

            data.user_id = request.user_id
            return func(request, data, *args, **kwargs)
        return wrapper
    return decorator

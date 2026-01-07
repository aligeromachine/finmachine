from collections.abc import Callable
from datetime import datetime, timedelta
from functools import wraps
import logging
from typing import Self
from pydantic import BaseModel, model_validator
from django.http import HttpRequest
from libs.dt.utils import time_parse
from libs.types.exp import F_Return, F_Spec
from libs.validate.exp import validate_dict_conv
from libs.const import CONST

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
            dt: datetime | None = time_parse(raw=self.created)
            if not dt:
                raise Exception(f"{self.created} does not match with {CONST.FormatFull}, {CONST.FormatJS}")

            self.created = dt
        return self

def draw_paginate(func: Callable[..., dict]) -> Callable[..., dict]:
    @wraps(func)
    def wrapper(*args: F_Spec.args, **kwargs: F_Spec.kwargs) -> dict:
        ls, count, offset, limit = func(*args, **kwargs)
        result: dict = dict(
            recordsTotal=count,
            offset=offset,
            recordsDisplay=limit,
            draw=ls
        )
        return result
    return wrapper

def validate_model(Model: type[MainModel]) -> Callable[..., Callable[..., F_Return | dict]]:
    def decorator(func: Callable[..., F_Return | dict]) -> Callable[..., F_Return | dict]:
        @wraps(func)
        def wrapper(request: HttpRequest, *args: F_Spec.args, **kwargs: F_Spec.kwargs) -> F_Return | dict:
            if not request.body:
                return {'data': 'err', 'message': 'body empty'}
            data: MainModel = validate_dict_conv(request.body, Model=Model, prn=True)
            if not data:
                return {'data': 'err', 'message': f'validate_dict_conv: {Model}'}
            data.user_id = request.user_id
            return func(request, data, *args, **kwargs)
        return wrapper
    return decorator

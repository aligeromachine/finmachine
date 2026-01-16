from collections.abc import Callable
from datetime import datetime, timedelta
from functools import wraps
import logging
from typing import Self
from pydantic import BaseModel, model_validator
from django.http import HttpRequest
from libs.model.exp import BaseModelWithRawArray
from libs.dt.utils import pretty_str, time_parse
from libs.types.exp import F_Spec
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

class BaseMessage(MainModel):
    offset: int = 0
    limit: int = 0
    pk: int = 0
    title: str = ''
    created: str | datetime = datetime.now() + timedelta(hours=3)

    @model_validator(mode='after')
    def base_message(self) -> Self:
        if isinstance(self.created, str) and self.created:
            dt: datetime | None = time_parse(raw=self.created)
            if not dt:
                raise Exception(f"{self.created} does not match with {CONST.FormatFull}, {CONST.FormatJS}")

            self.created = dt
        return self

class BaseSelector(BaseModelWithRawArray):
    id: int
    created: datetime | str
    title: str

    @model_validator(mode='after')
    def base_selector(self) -> Self:
        if isinstance(self.created, datetime):
            self.created = pretty_str(self.created)
        return self

def validate_model(Model: type[MainModel]) -> Callable[F_Spec, Callable[F_Spec, dict]]:  # type: ignore
    def decorator(func: Callable[F_Spec, dict]) -> Callable[F_Spec, dict]:  # type: ignore
        @wraps(func)
        def wrapper(request: HttpRequest, *args: F_Spec.args, **kwargs: F_Spec.kwargs) -> dict:
            if not request.body:
                return dict(data='err', message='body empty')
            data: MainModel = validate_dict_conv(request.body, Model=Model, prn=True)
            if not data:
                return dict(data='err', message=f'validate_dict_conv: {Model}')
            data.user_id = request.user_id
            rv: dict = func(request, data, *args, **kwargs)
            return rv
        return wrapper
    return decorator

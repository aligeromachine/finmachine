from collections.abc import Callable
from functools import wraps
import logging
from django.http import HttpRequest
from api.back.model import MainModel
from libs.types.exp import F_Spec
from libs.validate.exp import validate_dict_conv

logger = logging.getLogger(__name__)

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

from functools import wraps
from django.http import HttpRequest
from authentication.utils import verify_jwt_token
from libs.django.jsonResponse import ORJSONResponse
from libs.decore.response import token_response
from typing import Any, Callable

def jwt_auth_required(view_func: Callable[[HttpRequest], ORJSONResponse]) -> ORJSONResponse:
    @wraps(view_func)
    def wrapper(request: HttpRequest, *args: Any, **kwargs: Any) -> ORJSONResponse:
        # Get the token from the Authorization header
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return token_response(msg='Authorization header missing or invalid', code=401)

        token = auth_header.split(' ')[1]
        payload, err = verify_jwt_token(token)

        if err == "Token expired":
            return token_response(msg=err)

        if not payload:
            return token_response(msg=err, code=409)

        request.user_id = payload.get('user_id')
        return view_func(request, *args, **kwargs)
    return wrapper

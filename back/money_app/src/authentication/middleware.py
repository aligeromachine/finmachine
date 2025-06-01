from functools import wraps
from django.http import HttpRequest, JsonResponse
from authentication.utils import verify_jwt_token
from money.libs.decore import token_response

def jwt_auth_required(view_func):
    @wraps(view_func)
    def wrapper(request: HttpRequest, *args, **kwargs):
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

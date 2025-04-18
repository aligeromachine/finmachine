from functools import wraps
from django.utils.functional import SimpleLazyObject
from authentication.backends import JWTAuthenticationBackend
from django.http import HttpRequest, JsonResponse
from authentication.utils import verify_jwt_token

def jwt_auth_middleware(get_response):
    def middleware(request: HttpRequest):
        auth_header = request.headers.get('Authorization', '')
        if auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            user = SimpleLazyObject(lambda: JWTAuthenticationBackend().authenticate(request, token=token))
            request.user = user
        return get_response(request)
    return middleware


def jwt_auth_required(view_func):
    @wraps(view_func)
    def wrapper(request: HttpRequest, *args, **kwargs):
        # Get the token from the Authorization header
        auth_header = request.headers.get('Authorization')
        
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse(
                {'error': 'Authorization header missing or invalid'},
                status=401
            )
        
        token = auth_header.split(' ')[1]
        payload, err = verify_jwt_token(token)
        
        if not payload:
            return JsonResponse(
                {'error': err},
                status=401
            )
        
        return view_func(request, *args, **kwargs)
    
    return wrapper

from django.utils.functional import SimpleLazyObject
from authentication.backends import JWTAuthenticationBackend
from django.http import HttpRequest

def jwt_auth_middleware(get_response):
    def middleware(request: HttpRequest):
        auth_header = request.headers.get('Authorization', '')
        if auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            user = SimpleLazyObject(lambda: JWTAuthenticationBackend().authenticate(request, token=token))
            request.user = user
        return get_response(request)
    return middleware

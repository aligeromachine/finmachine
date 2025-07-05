from django.http import HttpRequest, JsonResponse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate
from authentication.utils import create_jwt_tokens, verify_jwt_token
from django.contrib.auth.models import User
from authentication.model import AuthLogin, AuthRefresh, AuthAccess, AuthRegister
from django.utils import timezone
from money.libs.decore import check_post, validate_auth, token_response
import logging

logger = logging.getLogger(__name__)

@check_post  # type: ignore
def custom_logout(request: HttpRequest) -> JsonResponse:
    return token_response(token={}, code=200)

@check_post  # type: ignore
@validate_auth(AuthLogin)  # type: ignore
def login_view(request: HttpRequest, data: AuthLogin) -> JsonResponse:

    user: AbstractUser = authenticate(request, username=data.username, password=data.password)
    if not user:
        return token_response(msg='Invalid credentials', code=401)
    # Update last_login field
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])

    tokens = create_jwt_tokens(user.pk)
    return token_response(token=tokens, code=200)

@check_post  # type: ignore
@validate_auth(AuthAccess)  # type: ignore
def protected_view(request: HttpRequest, data: AuthAccess) -> JsonResponse:

    payload, err = verify_jwt_token(token=data.access)
    if not payload:
        return token_response(msg=err, code=401)

    return token_response(token={'access': data.access})

@check_post  # type: ignore
@validate_auth(AuthRefresh)  # type: ignore
def refresh_token_view(request: HttpRequest, data: AuthRefresh) -> JsonResponse:

    payload, err = verify_jwt_token(token=data.refresh)
    if not payload:
        return token_response(msg=err, code=401)

    jwt_token = create_jwt_tokens(user_id=payload['user_id'])
    return token_response(token={'access': jwt_token['access']})

@check_post  # type: ignore
@validate_auth(AuthRegister)  # type: ignore
def register_view(request: HttpRequest, data: AuthRegister) -> JsonResponse:

    if User.objects.filter(username=data.username).exists():
        return token_response(msg='User already exist')

    user: AbstractUser = User.objects.create_user(
        username=data.username,
        password=data.password,
        email=data.email
    )
    if not user:
        return token_response(msg='User canot create')

    return token_response(token={'user_id': user.pk})

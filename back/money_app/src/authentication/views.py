from django.http import HttpRequest
from django.contrib.auth.models import AbstractUser
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from authentication.utils import check_post, parse_auth, create_jwt_tokens, token_response, verify_jwt_token
from django.contrib.auth.models import User
from authentication.model import AuthLogin, AuthRefresh, AuthAccess, AuthRegister

@check_post
def custom_logout(request: HttpRequest):
    request.session.flush()  # Clears the session completely
    response = redirect('login')
    # Set headers to prevent caching of the logout page
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

@check_post
@parse_auth(AuthLogin)
def login_view(request: HttpRequest, data: AuthLogin):
    
    user: AbstractUser = authenticate(request, username=data.username, password=data.password)
    if not user:
        return token_response(msg='Invalid credentials', code=401)
            
    tokens = create_jwt_tokens(user.pk)
    return token_response(token=tokens, code=200)

@check_post
@parse_auth(AuthAccess)
def protected_view(request: HttpRequest, data: AuthAccess):
    
    payload, err = verify_jwt_token(token=data.access)
    if not payload:
        return token_response(msg=err, code=401)
    
    return token_response(token={'access': data.access})

@check_post
@parse_auth(AuthRefresh)
def refresh_token_view(request: HttpRequest, data: AuthRefresh):
    
    payload, err = verify_jwt_token(token=data.refresh)
    if not payload:
        return token_response(msg=err, code=401)
    
    jwt_token = create_jwt_tokens(user_id=payload['user_id'])
    return token_response(token={'access': jwt_token['access']})
    
@check_post
@parse_auth(AuthRegister)
def register_view(request: HttpRequest, data: AuthRegister):
    
    if User.objects.filter(username=data.username).exists():
        return token_response(msg='User alredy exist', code=402)
        
    user: AbstractUser = User.objects.create_user(
        username=data.username,
        password=data.password,
        email=data.email
    )
    if not user:
        return token_response(msg='User canot create', code=403)
    
    return token_response(token={'user_id': user.pk})

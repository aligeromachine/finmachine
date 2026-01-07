from typing import Any
from django.http import JsonResponse, HttpRequest
from authentication.middleware import jwt_auth_required
from api.back.dash.main import invoke_response
from libs.decore.response import check_post

@jwt_auth_required  # type: ignore
@check_post  # type: ignore
def content_respo(request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse:
    data = invoke_response(request=request)
    return JsonResponse(data)

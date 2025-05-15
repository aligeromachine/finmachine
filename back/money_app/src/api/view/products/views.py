from django.http import JsonResponse, HttpRequest
from authentication.middleware import jwt_auth_required
from money.libs.decore import check_post
from api.back.products.main import invoke_response

@jwt_auth_required
@check_post
def content_respo(request: HttpRequest, *args, **kwargs):

    data = invoke_response(request=request)

    return JsonResponse(data, safe=False)

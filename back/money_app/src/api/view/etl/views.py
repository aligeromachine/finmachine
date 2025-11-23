from typing import Any
from django.http import JsonResponse, HttpRequest
from api.back.etl.main import update_money_csv


def content_respo(request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse:
    data = update_money_csv()
    return JsonResponse(data)

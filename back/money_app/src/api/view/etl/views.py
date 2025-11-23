from typing import Any
from django.http import JsonResponse, HttpRequest
from api.back.etl.main import audit_money_history, update_money_csv


def content_respo(request: HttpRequest, name: str, *args: Any, **kwargs: Any) -> JsonResponse:
    print(name)
    data: dict = {}
    if name == 'etl':
        data = update_money_csv()
    if name == 'cel':
        data = audit_money_history()

    return JsonResponse(data)

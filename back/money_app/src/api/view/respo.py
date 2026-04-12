from typing import Any
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from authentication.middleware import jwt_auth_required
from libs.django.jsonResponse import ORJSONResponse
from service.settings import VERSION
from api.back.buy.main import invoke_response as buy_response
from api.back.dash.main import invoke_response as dash_response
from api.back.logger.main import invoke_response as logger_response
from api.back.source.main import invoke_response as source_response
from api.back.shop.main import invoke_response as shop_response
from api.back.profit.main import invoke_response as profit_response
from api.back.products.main import invoke_response as products_response
from api.back.catalog.main import invoke_response as catalog_response
from api.back.cards.main import invoke_response as cards_response
from api.back.etl.main import audit_money_history, update_money_csv

@csrf_exempt  # type: ignore
def version_respo(request: HttpRequest, *args: Any, **kwargs: Any) -> ORJSONResponse:
    return ORJSONResponse(data=dict(version=VERSION))

@jwt_auth_required  # type: ignore
def dash_respo(request: HttpRequest, *args: Any, **kwargs: Any) -> ORJSONResponse:
    return ORJSONResponse(data=dash_response(request=request), safe=False)

@jwt_auth_required  # type: ignore
def logger_respo(request: HttpRequest, *args: Any, **kwargs: Any) -> ORJSONResponse:
    return ORJSONResponse(data=logger_response(request=request), safe=False)

@jwt_auth_required  # type: ignore
def buy_respo(request: HttpRequest, *args: Any, **kwargs: Any) -> ORJSONResponse:
    return ORJSONResponse(data=buy_response(request=request), safe=False)

@jwt_auth_required  # type: ignore
def source_respo(request: HttpRequest, *args: Any, **kwargs: Any) -> ORJSONResponse:
    data = source_response(request=request)
    return ORJSONResponse(data, safe=False)

@jwt_auth_required  # type: ignore
def shop_respo(request: HttpRequest, *args: Any, **kwargs: Any) -> ORJSONResponse:
    return ORJSONResponse(data=shop_response(request=request), safe=False)

@jwt_auth_required  # type: ignore
def profit_respo(request: HttpRequest, *args: Any, **kwargs: Any) -> ORJSONResponse:
    return ORJSONResponse(data=profit_response(request=request), safe=False)

@jwt_auth_required  # type: ignore
def products_respo(request: HttpRequest, *args: Any, **kwargs: Any) -> ORJSONResponse:
    return ORJSONResponse(data=products_response(request=request), safe=False)

@jwt_auth_required  # type: ignore
def catalog_respo(request: HttpRequest, *args: Any, **kwargs: Any) -> ORJSONResponse:
    return ORJSONResponse(data=catalog_response(request=request), safe=False)

@jwt_auth_required  # type: ignore
def cards_respo(request: HttpRequest, *args: Any, **kwargs: Any) -> ORJSONResponse:
    return ORJSONResponse(data=cards_response(request=request), safe=False)


def etl_respo(request: HttpRequest, name: str, *args: Any, **kwargs: Any) -> ORJSONResponse:
    print(name)
    data: dict = {}
    if name == 'etl':
        data = update_money_csv()
    if name == 'cel':
        data = audit_money_history()

    return ORJSONResponse(data)

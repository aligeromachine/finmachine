from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.decore import draw_response
from money.libs.ext_utils import timeDRFF
from money.models import Products
from api.model.products import ProductsMessage
from api.back.products.query import SQL_PRODUCTS, PRODUCTS_TOTAL

logger = logging.getLogger(__name__)

@draw_response
def update_profit_data(item: ProductsMessage):
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = []
    for it in Products.objects.raw(raw_query=SQL_PRODUCTS, params=params):
        raw = {
            'id': it.id,
            'created': timeDRFF(it.created),
            'title': it.title,
            'cats': it.cats,
        }
        ls.append(raw)

    params = [item.user_id]
    count: int = 0
    for it in Products.objects.raw(raw_query=PRODUCTS_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

@validate_model(ProductsMessage)
def invoke_response(request: HttpRequest, item: ProductsMessage):
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "update_profit_data":
        respo = update_profit_data(item=item)

    return respo

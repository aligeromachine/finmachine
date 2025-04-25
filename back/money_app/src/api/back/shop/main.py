from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.decore import draw_response
from money.libs.ext_utils import timeDRFF
from money.models import Cards
from api.model.shop import ShopMessage
from api.back.shop.query import SQL_SHOP, SHOP_TOTAL

logger = logging.getLogger(__name__)

@draw_response
def update_shop_data(item: ShopMessage):
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = []
    for it in Cards.objects.raw(raw_query=SQL_SHOP, params=params):
        raw = {
            'id': it.id,
            'created': timeDRFF(it.created),
            'title': it.title,
            'address': it.address,
        }
        ls.append(raw)

    params = [item.user_id]
    count: int = 0
    for it in Cards.objects.raw(raw_query=SHOP_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

@validate_model(ShopMessage)
def invoke_response(request: HttpRequest, item: ShopMessage):
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "update_shop_data":
        respo = update_shop_data(item=item)

    return respo

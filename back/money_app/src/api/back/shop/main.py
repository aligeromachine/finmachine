from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.decore import draw_response
from money.utils.func import model_max_id
from money.libs.ext_utils import timeDRFF
from money.models import Shop
from api.model.shop import ShopMessage
from api.back.shop.query import SQL_SHOP, SHOP_TOTAL

logger = logging.getLogger(__name__)

@draw_response
def update_shop_data(item: ShopMessage):
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = []
    for it in Shop.objects.raw(raw_query=SQL_SHOP, params=params):
        raw = {
            'id': it.id,
            'created': timeDRFF(it.created),
            'title': it.title,
            'address': it.address,
        }
        ls.append(raw)

    params = [item.user_id]
    count: int = 0
    for it in Shop.objects.raw(raw_query=SHOP_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

def add_shop_data(item: ShopMessage):
    Shop(title=item.title, address=item.address, user_id=item.user_id).save()
    max_id = model_max_id(model=Shop)

    return {'data': 'ok', 'message': f'adding shop key: {max_id}'}

@validate_model(ShopMessage)
def invoke_response(request: HttpRequest, item: ShopMessage):
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "update_shop_data":
        respo = update_shop_data(item=item)
    
    if item.command == "add_shop_data":
        respo = add_shop_data(item=item)

    return respo

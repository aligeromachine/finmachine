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
def table_shop_data(item: ShopMessage):
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

def delete_shop_row(item: ShopMessage):
    Shop.objects.filter(pk=item.pk).delete()
    return {'data': 'ok', 'message': f'delete shop key: {item.pk}'}

def get_shop_row(item: ShopMessage):
    data = {}

    for it in Shop.objects.filter(pk=item.pk):
        data["title"] = it.title
        data["address"] = it.address

    return data

def edit_shop_data(item: ShopMessage):
    try:
        instance = Shop.objects.get(pk=item.pk)

        instance.title = item.title
        instance.address = item.address
        instance.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}

@validate_model(ShopMessage)
def invoke_response(request: HttpRequest, item: ShopMessage):
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "table_shop_data":
        respo = table_shop_data(item=item)
    
    if item.command == "add_shop_data":
        respo = add_shop_data(item=item)
    
    if item.command == "delete_shop_row":
        respo = delete_shop_row(item=item)
    
    if item.command == "get_shop_row":
        respo = get_shop_row(item=item)
    
    if item.command == "edit_shop_data":
        respo = edit_shop_data(item=item)

    return respo

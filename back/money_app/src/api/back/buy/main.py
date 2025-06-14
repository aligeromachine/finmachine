from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.decore import draw_response
from money.utils.func import model_max_id
from money.libs.ext_utils import dateDRF
from money.models import Buy
from api.model.buy import BuyMessage
from api.back.buy.query import BUY_ROW, SQL_BUY, BUY_TOTAL

logger = logging.getLogger(__name__)

@draw_response
def table_buy_data(item: BuyMessage):
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = []
    for it in Buy.objects.raw(raw_query=SQL_BUY, params=params):
        raw = {
            'id': it.id,
            'created': dateDRF(it.created),
            'title': it.title,
            'amount': it.amount,
            'shop': it.shop,
            'cat': it.cat,
            'prod': it.prod,
        }
        ls.append(raw)

    params = [item.user_id]
    count: int = 0
    for it in Buy.objects.raw(raw_query=BUY_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

def add_buy_data(item: BuyMessage):
    Buy(
        title=item.title,
        amount=item.amount,
        shop_id=item.shop,
        products_id=item.prod,
        user_id=item.user_id
    ).save()
    max_id = model_max_id(model=Buy)

    return {'data': 'ok', 'message': f'adding Buy key: {max_id}'}

def delete_buy_row(item: BuyMessage):
    Buy.objects.filter(pk=item.pk).delete()
    return {'data': 'ok', 'message': f'delete Buy key: {item.pk}'}

def get_buy_row(item: BuyMessage):
    data = {}

    for it in Buy.objects.raw(raw_query=BUY_ROW, params=[item.pk]):
        data["title"] = it.title
        data["amount"] = it.amount
        data["shop"] = it.shop
        data["cat"] = it.cat
        data["prod"] = it.prod

    return data

def edit_buy_data(item: BuyMessage):
    try:
        instance = Buy.objects.get(pk=item.pk)

        instance.title = item.title
        instance.amount = item.amount
        instance.shop_id = item.shop
        instance.products_id = item.prod
        instance.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}

@validate_model(BuyMessage)
def invoke_response(request: HttpRequest, item: BuyMessage):
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "table_buy_data":
        respo = table_buy_data(item=item)

    if item.command == "add_buy_data":
        respo = add_buy_data(item=item)

    if item.command == "delete_buy_row":
        respo = delete_buy_row(item=item)

    if item.command == "get_buy_row":
        respo = get_buy_row(item=item)

    if item.command == "edit_buy_data":
        respo = edit_buy_data(item=item)

    return respo

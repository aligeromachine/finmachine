from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.decore import draw_response
from money.libs.ext_utils import timeDRFF
from money.models import Buy
from api.model.buy import BuyMessage
from api.back.buy.query import SQL_BUY, BUY_TOTAL

logger = logging.getLogger(__name__)

@draw_response
def update_money_data(item: BuyMessage):
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = []
    for it in Buy.objects.raw(raw_query=SQL_BUY, params=params):
        raw = {
            'id': it.id,
            'created': timeDRFF(it.created),
            'title': it.title,
            'amount': it.amount,
            'shop': it.shop,
            'prod': it.prod,
        }
        ls.append(raw)

    params = [item.user_id]
    count: int = 0
    for it in Buy.objects.raw(raw_query=BUY_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

@validate_model(BuyMessage)
def invoke_response(request: HttpRequest, item: BuyMessage):
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "update_money_data":
        respo = update_money_data(item=item)

    return respo

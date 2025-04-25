from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.decore import draw_response
from money.libs.ext_utils import timeDRFF
from money.models import Profit
from api.model.profit import ProfitMessage
from api.back.profit.query import SQL_PROFIT, PROFIT_TOTAL

logger = logging.getLogger(__name__)

@draw_response
def update_profit_data(item: ProfitMessage):
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = []
    for it in Profit.objects.raw(raw_query=SQL_PROFIT, params=params):
        raw = {
            'id': it.id,
            'created': timeDRFF(it.created),
            'title': it.title,
            'sources': it.sources,
        }
        ls.append(raw)

    params = [item.user_id]
    count: int = 0
    for it in Profit.objects.raw(raw_query=PROFIT_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit


@validate_model(ProfitMessage)
def invoke_response(request: HttpRequest, item: ProfitMessage):
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "update_profit_data":
        respo = update_profit_data(item=item)

    return respo

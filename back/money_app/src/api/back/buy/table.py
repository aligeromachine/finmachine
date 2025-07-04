import logging
from api.back.decore import draw_paginate
from api.back.buy.model import BuyMessage, BuySelector
from money.models import Buy
from api.back.buy.query import SQL_BUY, BUY_TOTAL

logger = logging.getLogger(__name__)

@draw_paginate  # type: ignore
def table_buy_data(item: BuyMessage) -> tuple:
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = [BuySelector.from_orm(it).model_dump() for it in Buy.objects.raw(raw_query=SQL_BUY, params=params)]

    params = [item.user_id]
    count: int = 0
    for it in Buy.objects.raw(raw_query=BUY_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

import logging
from libs.decore.utils import draw_paginate
from libs.django.base import count_raw_sql
from api.back.buy.model import BuyMessage, BuySelector
from money.models import Buy
from api.back.buy.query import SQL_BUY, BUY_TOTAL

logger = logging.getLogger(__name__)

@draw_paginate  # type: ignore
def table_buy_data(item: BuyMessage) -> tuple:
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = [BuySelector.from_orm(it).model_dump() for it in Buy.objects.raw(raw_query=SQL_BUY, params=params)]
    count: int = count_raw_sql(model=Buy, sql=BUY_TOTAL, params=[item.user_id])

    return ls, count, item.offset, item.limit

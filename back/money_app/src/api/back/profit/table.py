import logging
from libs.django.base import count_raw_sql
from libs.decore.utils import draw_paginate
from api.back.profit.model import ProfitMessage, ProfitSelector
from money.models import Profit
from api.back.profit.query import SQL_PROFIT, PROFIT_TOTAL

logger = logging.getLogger(__name__)

@draw_paginate  # type: ignore
def table_profit_data(item: ProfitMessage) -> tuple:
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = [ProfitSelector.from_orm(it).model_dump() for it in Profit.objects.raw(raw_query=SQL_PROFIT, params=params)]
    count: int = count_raw_sql(model=Profit, sql=PROFIT_TOTAL, params=[item.user_id])

    return ls, count, item.offset, item.limit

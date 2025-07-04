import logging
from api.back.decore import draw_paginate
from api.back.shop.model import ShopMessage, ShopSelector
from money.models import Shop
from api.back.shop.query import SQL_SHOP, SHOP_TOTAL

logger = logging.getLogger(__name__)

@draw_paginate
def table_shop_data(item: ShopMessage) -> dict:
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = [ShopSelector.from_orm(it).model_dump() for it in Shop.objects.raw(raw_query=SQL_SHOP, params=params)]

    params = [item.user_id]
    count: int = 0
    for it in Shop.objects.raw(raw_query=SHOP_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

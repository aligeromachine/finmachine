import logging
from libs.django.base import count_raw_sql
from libs.decore.utils import draw_paginate
from api.back.shop.model import ShopMessage, ShopSelector
from money.models import Shop
from api.back.shop.query import SQL_SHOP, SHOP_TOTAL

logger = logging.getLogger(__name__)

@draw_paginate  # type: ignore
def table_shop_data(item: ShopMessage) -> tuple:
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = [ShopSelector.from_orm(it).model_dump() for it in Shop.objects.raw(raw_query=SQL_SHOP, params=params)]
    count: int = count_raw_sql(model=Shop, sql=SHOP_TOTAL, params=[item.user_id])

    return ls, count, item.offset, item.limit

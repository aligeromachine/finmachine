import logging
from api.back.decore import draw_paginate
from api.back.products.model import ProdSelector, ProductsMessage
from money.models import Products
from api.back.products.query import SQL_PRODUCTS, PRODUCTS_TOTAL

logger = logging.getLogger(__name__)

@draw_paginate  # type: ignore
def table_prod_data(item: ProductsMessage) -> tuple:
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = [ProdSelector.from_orm(it).model_dump() for it in Products.objects.raw(raw_query=SQL_PRODUCTS, params=params)]

    params = [item.user_id]
    count: int = 0
    for it in Products.objects.raw(raw_query=PRODUCTS_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

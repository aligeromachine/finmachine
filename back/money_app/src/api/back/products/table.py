import logging
from libs.django.base import count_raw_sql
from libs.decore.utils import draw_paginate
from api.back.products.model import ProdSelector, ProductsMessage
from money.models import Products
from api.back.products.query import SQL_PRODUCTS, PRODUCTS_TOTAL

logger = logging.getLogger(__name__)

@draw_paginate  # type: ignore
def table_prod_data(item: ProductsMessage) -> tuple:
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = [ProdSelector.from_orm(it).model_dump() for it in Products.objects.raw(raw_query=SQL_PRODUCTS, params=params)]
    count: int = count_raw_sql(model=Products, sql=PRODUCTS_TOTAL, params=[item.user_id])

    return ls, count, item.offset, item.limit

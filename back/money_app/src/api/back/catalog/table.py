import logging
from api.back.decore import draw_paginate
from api.back.catalog.model import CatSelector, CatalogMessage
from money.models import Catalog
from api.back.catalog.query import SQL_CATALOG, CATALOG_TOTAL

logger = logging.getLogger(__name__)

@draw_paginate  # type: ignore
def table_cat_data(item: CatalogMessage) -> tuple:
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = [CatSelector.from_orm(it).model_dump() for it in Catalog.objects.raw(raw_query=SQL_CATALOG, params=params)]

    params = [item.user_id]
    count: int = 0
    for it in Catalog.objects.raw(raw_query=CATALOG_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

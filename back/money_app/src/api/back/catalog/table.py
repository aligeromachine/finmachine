import logging
from libs.django.base import count_raw_sql
from libs.decore.utils import draw_paginate
from api.back.catalog.model import CatSelector, CatalogMessage
from money.models import Catalog
from api.back.catalog.query import SQL_CATALOG, CATALOG_TOTAL

logger = logging.getLogger(__name__)

@draw_paginate  # type: ignore
def table_cat_data(item: CatalogMessage) -> tuple:
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = [CatSelector.from_orm(it).model_dump() for it in Catalog.objects.raw(raw_query=SQL_CATALOG, params=params)]
    count: int = count_raw_sql(model=Catalog, sql=CATALOG_TOTAL, params=[item.user_id])

    return ls, count, item.offset, item.limit

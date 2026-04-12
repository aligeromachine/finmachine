import logging
from libs.django.base import count_raw_sql
from libs.decore.utils import draw_paginate
from api.back.source.model import SourceMessage, SourceSelector
from money.models import Source
from api.back.source.query import SQL_SOURCE, SOURCE_TOTAL

logger = logging.getLogger(__name__)

@draw_paginate  # type: ignore
def table_source_data(item: SourceMessage) -> tuple:
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = [SourceSelector.from_orm(it).model_dump() for it in Source.objects.raw(raw_query=SQL_SOURCE, params=params)]
    count: int = count_raw_sql(model=Source, sql=SOURCE_TOTAL, params=[item.user_id])

    return ls, count, item.offset, item.limit

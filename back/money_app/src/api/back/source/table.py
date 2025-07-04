import logging
from api.back.decore import draw_paginate
from api.back.source.model import SourceMessage, SourceSelector
from money.models import Source
from api.back.source.query import SQL_SOURCE, SOURCE_TOTAL

logger = logging.getLogger(__name__)

@draw_paginate
def table_source_data(item: SourceMessage) -> dict:
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = [SourceSelector.from_orm(it).model_dump() for it in Source.objects.raw(raw_query=SQL_SOURCE, params=params)]

    params = [item.user_id]
    count: int = 0
    for it in Source.objects.raw(raw_query=SOURCE_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.decore import draw_response
from money.libs.ext_utils import timeDRFF
from money.models import Source
from api.model.source import SourceMessage
from api.back.source.query import SQL_SOURCE, SOURCE_TOTAL

logger = logging.getLogger(__name__)

@draw_response
def update_source_data(item: SourceMessage):
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = []
    for it in Source.objects.raw(raw_query=SQL_SOURCE, params=params):
        raw = {
            'id': it.id,
            'created': timeDRFF(it.created),
            'title': it.title,
        }
        ls.append(raw)

    params = [item.user_id]
    count: int = 0
    for it in Source.objects.raw(raw_query=SOURCE_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

@validate_model(SourceMessage)
def invoke_response(request: HttpRequest, item: SourceMessage):
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "update_source_data":
        respo = update_source_data(item=item)

    return respo

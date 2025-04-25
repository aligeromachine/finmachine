from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.decore import draw_response
from money.libs.ext_utils import timeDRFF
from money.models import Catalog
from api.model.catalog import CatalogMessage
from api.back.catalog.query import SQL_CATALOG, CATALOG_TOTAL

logger = logging.getLogger(__name__)

@draw_response
def update_catalog_data(item: CatalogMessage):
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = []
    for it in Catalog.objects.raw(raw_query=SQL_CATALOG, params=params):
        raw = {
            'id': it.id,
            'created': timeDRFF(it.created),
            'title': it.title
        }
        ls.append(raw)

    params = [item.user_id]
    count: int = 0
    for it in Catalog.objects.raw(raw_query=CATALOG_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

@validate_model(CatalogMessage)
def invoke_response(request: HttpRequest, item: CatalogMessage):
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "update_catalog_data":
        respo = update_catalog_data(item=item)

    return respo

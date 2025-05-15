from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.decore import draw_response
from money.utils.func import model_max_id
from money.libs.ext_utils import dateDRF
from money.models import Catalog
from api.model.catalog import CatalogMessage
from api.back.catalog.query import SQL_CATALOG, CATALOG_TOTAL

logger = logging.getLogger(__name__)

@draw_response
def table_cat_data(item: CatalogMessage):
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = []
    for it in Catalog.objects.raw(raw_query=SQL_CATALOG, params=params):
        raw = {
            'id': it.id,
            'created': dateDRF(it.created),
            'title': it.title
        }
        ls.append(raw)

    params = [item.user_id]
    count: int = 0
    for it in Catalog.objects.raw(raw_query=CATALOG_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

def add_cat_data(item: CatalogMessage):
    Catalog(
        title=item.title,
        user_id=item.user_id
    ).save()
    max_id = model_max_id(model=Catalog)

    return {'data': 'ok', 'message': f'adding Catalog key: {max_id}'}

def delete_cat_row(item: CatalogMessage):
    Catalog.objects.filter(pk=item.pk).delete()
    return {'data': 'ok', 'message': f'delete Catalog key: {item.pk}'}

def get_cat_row(item: CatalogMessage):
    data = {}

    for it in Catalog.objects.filter(pk=item.pk):
        data["title"] = it.title

    return data

def edit_cat_data(item: CatalogMessage):
    try:
        instance = Catalog.objects.get(pk=item.pk)

        instance.title = item.title
        instance.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}

def list_cat_data(item: CatalogMessage):
    ls: list = []

    for it in Catalog.objects.all():
        ls.append({"pk": it.pk, "title": it.title})

    return ls

@validate_model(CatalogMessage)
def invoke_response(request: HttpRequest, item: CatalogMessage):
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "table_cat_data":
        respo = table_cat_data(item=item)

    if item.command == "add_cat_data":
        respo = add_cat_data(item=item)

    if item.command == "delete_cat_row":
        respo = delete_cat_row(item=item)

    if item.command == "get_cat_row":
        respo = get_cat_row(item=item)

    if item.command == "edit_cat_data":
        respo = edit_cat_data(item=item)

    if item.command == "list_cat_data":
        respo = list_cat_data(item=item)

    return respo

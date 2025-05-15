from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.decore import draw_response
from money.utils.func import model_max_id
from money.libs.ext_utils import dateDRF
from money.models import Source
from api.model.source import SourceMessage
from api.back.source.query import SQL_SOURCE, SOURCE_TOTAL

logger = logging.getLogger(__name__)

@draw_response
def table_source_data(item: SourceMessage):
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = []
    for it in Source.objects.raw(raw_query=SQL_SOURCE, params=params):
        raw = {
            'id': it.id,
            'created': dateDRF(it.created),
            'title': it.title,
        }
        ls.append(raw)

    params = [item.user_id]
    count: int = 0
    for it in Source.objects.raw(raw_query=SOURCE_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

def add_source_data(item: SourceMessage):
    Source(title=item.title, user_id=item.user_id).save()
    max_id = model_max_id(model=Source)

    return {'data': 'ok', 'message': f'adding Source key: {max_id}'}

def delete_source_row(item: SourceMessage):
    Source.objects.filter(pk=item.pk).delete()
    return {'data': 'ok', 'message': f'delete Source key: {item.pk}'}

def get_source_row(item: SourceMessage):
    data = {}

    for it in Source.objects.filter(pk=item.pk):
        data["title"] = it.title

    return data

def edit_source_data(item: SourceMessage):
    try:
        instance = Source.objects.get(pk=item.pk)

        instance.title = item.title
        instance.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}

def list_source_data(item: SourceMessage):
    ls: list = []

    for it in Source.objects.all():
        ls.append({"pk": it.pk, "title": it.title})

    return ls

@validate_model(SourceMessage)
def invoke_response(request: HttpRequest, item: SourceMessage):
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "table_source_data":
        respo = table_source_data(item=item)

    if item.command == "add_source_data":
        respo = add_source_data(item=item)

    if item.command == "delete_source_row":
        respo = delete_source_row(item=item)

    if item.command == "get_source_row":
        respo = get_source_row(item=item)

    if item.command == "edit_source_data":
        respo = edit_source_data(item=item)

    if item.command == "list_source_data":
        respo = list_source_data(item=item)

    return respo

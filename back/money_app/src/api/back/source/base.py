import logging
from api.back.source.model import SourceMessage, SourceSignal, SourceSignalKV
from api.back.source.query import SOURCE_SORTED
from money.models import Source

logger = logging.getLogger(__name__)

def add_source_data(item: SourceMessage) -> dict:
    elem = Source.objects.create(title=item.title, user_id=item.user_id)
    elem.created = item.created
    elem.save()
    return {'data': 'ok', 'message': f'adding Source key: {elem.pk}'}

def delete_source_row(item: SourceMessage) -> dict:
    Source.objects.filter(pk=item.pk).delete()
    return {'data': 'ok', 'message': f'delete Source key: {item.pk}'}

def get_source_row(item: SourceMessage) -> dict:
    data: dict = {}
    for it in Source.objects.filter(pk=item.pk):
        data = SourceSignal.from_orm(it).model_dump()
    return data

def edit_source_data(item: SourceMessage) -> dict:
    try:
        elem = Source.objects.get(pk=item.pk)

        elem.title = item.title
        elem.created = item.created
        elem.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}

def list_source_data(item: SourceMessage) -> list:
    sql: str = SOURCE_SORTED
    params = [item.user_id]
    ls: list = [SourceSignalKV.from_orm(it).model_dump() for it in Source.objects.raw(raw_query=sql, params=params)]
    return ls

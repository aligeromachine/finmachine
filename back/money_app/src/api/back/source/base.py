import logging
from api.back.source.model import SourceMessage, SourceSignal, SourceSignalKV
from money.utils.func import model_max_id
from money.models import Source

logger = logging.getLogger(__name__)

def add_source_data(item: SourceMessage) -> dict:
    Source(title=item.title, user_id=item.user_id).save()
    max_id = model_max_id(model=Source)

    return {'data': 'ok', 'message': f'adding Source key: {max_id}'}

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
        instance = Source.objects.get(pk=item.pk)

        instance.title = item.title
        instance.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}

def list_source_data(item: SourceMessage) -> list:
    ls: list = [SourceSignalKV.from_orm(it).model_dump() for it in Source.objects.filter(user=item.user_id)]
    return ls

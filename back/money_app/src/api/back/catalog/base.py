import logging
from api.back.catalog.model import CatSignal, CatSignalKV, CatalogMessage
from money.utils.func import model_max_id
from money.models import Catalog

logger = logging.getLogger(__name__)

def add_cat_data(item: CatalogMessage) -> dict:
    Catalog(
        title=item.title,
        user_id=item.user_id
    ).save()
    max_id = model_max_id(model=Catalog)

    return {'data': 'ok', 'message': f'adding Catalog key: {max_id}'}

def delete_cat_row(item: CatalogMessage) -> dict:
    Catalog.objects.filter(pk=item.pk).delete()
    return {'data': 'ok', 'message': f'delete Catalog key: {item.pk}'}

def get_cat_row(item: CatalogMessage):
    data: dict = {}
    for it in Catalog.objects.filter(pk=item.pk):
        data = CatSignal.from_orm(it).model_dump()
    return data

def edit_cat_data(item: CatalogMessage) -> dict:
    try:
        instance = Catalog.objects.get(pk=item.pk)

        instance.title = item.title
        instance.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}

def list_cat_data(item: CatalogMessage) -> list:
    ls: list = [CatSignalKV.from_orm(it).model_dump() for it in Catalog.objects.all()]
    return ls

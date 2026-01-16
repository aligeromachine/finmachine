import logging
from api.back.catalog.model import CatSignal, CatSignalKV, CatalogMessage
from api.back.catalog.query import SQL_CATALOG_SORT
from money.models import Catalog

logger = logging.getLogger(__name__)

def add_cat_data(item: CatalogMessage) -> dict:
    elem = Catalog.objects.create(title=item.title, user_id=item.user_id)
    elem.created = item.created
    elem.save()
    return dict(data='ok', message=f'adding {item.__name__} key: {elem.pk}')

def delete_cat_row(item: CatalogMessage) -> dict:
    Catalog.objects.filter(pk=item.pk).delete()
    return dict(data='ok', message=f'delete Catalog key: {item.pk}')

def get_cat_row(item: CatalogMessage) -> dict:
    data: dict = {}
    for it in Catalog.objects.filter(pk=item.pk):
        data = CatSignal.from_orm(it).model_dump()
    return data

def edit_cat_data(item: CatalogMessage) -> dict:
    try:
        elem = Catalog.objects.get(pk=item.pk)

        elem.title = item.title
        elem.created = item.created
        elem.save()
    except: # noqa
        return dict(data='err', message='pk does not exist')

    return dict(data='ok', message=f'update {item.pk=}')

def list_cat_data(item: CatalogMessage) -> list:
    ls: list = [CatSignalKV.from_orm(it).model_dump() for it in Catalog.objects.raw(SQL_CATALOG_SORT, params=[item.user_id])]
    return ls

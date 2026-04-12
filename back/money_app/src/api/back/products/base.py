import logging
from api.back.products.model import ProdSignal, ProdSignalKV, ProductsMessage
from api.back.products.query import PRODUCTS_SORTED
from money.models import Products

logger = logging.getLogger(__name__)

def add_prod_data(item: ProductsMessage) -> dict:
    elem = Products.objects.create(title=item.title, catalog_id=item.catalog, user_id=item.user_id)
    elem.created = item.created
    elem.save()
    return dict(data='ok', message=f'adding Products key: {elem.pk}')

def delete_prod_row(item: ProductsMessage) -> dict:
    Products.objects.filter(pk=item.pk).delete()
    return dict(data='ok', message=f'delete Products key: {item.pk}')

def get_prod_row(item: ProductsMessage) -> dict:
    data: dict = {}
    for it in Products.objects.filter(pk=item.pk):
        data = ProdSignal.from_orm(it).model_dump()
    return data

def edit_prod_data(item: ProductsMessage) -> dict:
    try:
        elem = Products.objects.get(pk=item.pk)

        elem.title = item.title
        elem.catalog_id = item.catalog
        elem.created = item.created
        elem.save()
    except: # noqa
        return dict(data='err', message='pk does not exist')

    return dict(data='ok', message=f'update {item.pk=}')

def list_prod_data(item: ProductsMessage) -> list:
    sql = PRODUCTS_SORTED
    params = [item.user_id, item.pk]
    ls: list = [ProdSignalKV.from_orm(it).model_dump() for it in Products.objects.raw(raw_query=sql, params=params)]
    return ls

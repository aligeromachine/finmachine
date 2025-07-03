import logging
from api.back.products.model import ProdSignal, ProdSignalKV, ProductsMessage
from api.back.products.query import PRODUCTS_ROW
from money.utils.func import model_max_id
from money.models import Products

logger = logging.getLogger(__name__)

def add_prod_data(item: ProductsMessage) -> dict:
    Products(
        title=item.title,
        catalog_id=item.catalog,
        user_id=item.user_id
    ).save()
    max_id = model_max_id(model=Products)

    return {'data': 'ok', 'message': f'adding Products key: {max_id}'}

def delete_prod_row(item: ProductsMessage) -> dict:
    Products.objects.filter(pk=item.pk).delete()
    return {'data': 'ok', 'message': f'delete Products key: {item.pk}'}

def get_prod_row(item: ProductsMessage) -> dict:
    data: dict = {}
    for it in Products.objects.raw(raw_query=PRODUCTS_ROW, params=[item.pk]):
        data = ProdSignal.from_orm(it).model_dump()
    return data

def edit_prod_data(item: ProductsMessage) -> dict:
    try:
        instance = Products.objects.get(pk=item.pk)

        instance.title = item.title
        instance.catalog_id = item.catalog
        instance.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}

def list_prod_data(item: ProductsMessage) -> dict:
    ls: list = [ProdSignalKV.from_orm(it).model_dump() for it in Products.objects.filter(catalog_id=item.pk)]
    return ls

from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.decore import draw_response
from money.utils.func import model_max_id
from money.libs.ext_utils import dateDRF
from money.models import Products
from api.model.products import ProductsMessage
from api.back.products.query import SQL_PRODUCTS, PRODUCTS_TOTAL

logger = logging.getLogger(__name__)

@draw_response
def table_prod_data(item: ProductsMessage):
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = []
    for it in Products.objects.raw(raw_query=SQL_PRODUCTS, params=params):
        raw = {
            'id': it.id,
            'created': dateDRF(it.created),
            'title': it.title,
            'catalog': it.cat,
        }
        ls.append(raw)

    params = [item.user_id]
    count: int = 0
    for it in Products.objects.raw(raw_query=PRODUCTS_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

def add_prod_data(item: ProductsMessage):
    Products(
        title=item.title,
        catalog_id=item.catalog,
        user_id=item.user_id
    ).save()
    max_id = model_max_id(model=Products)

    return {'data': 'ok', 'message': f'adding Products key: {max_id}'}

def delete_prod_row(item: ProductsMessage):
    Products.objects.filter(pk=item.pk).delete()
    return {'data': 'ok', 'message': f'delete Products key: {item.pk}'}

def get_prod_row(item: ProductsMessage):
    data = {}

    for it in Products.objects.filter(pk=item.pk):
        data["title"] = it.title
        data["catalog"] = it.catalog_id

    return data

def edit_prod_data(item: ProductsMessage):
    try:
        instance = Products.objects.get(pk=item.pk)

        instance.title = item.title
        instance.catalog_id = item.catalog
        instance.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}

def list_prod_data(item: ProductsMessage):
    ls: list = []

    for it in Products.objects.filter(catalog_id=item.pk):
        ls.append({"pk": it.pk, "title": it.title})

    return ls

@validate_model(ProductsMessage)
def invoke_response(request: HttpRequest, item: ProductsMessage):
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "table_prod_data":
        respo = table_prod_data(item=item)

    if item.command == "add_prod_data":
        respo = add_prod_data(item=item)

    if item.command == "delete_prod_row":
        respo = delete_prod_row(item=item)

    if item.command == "get_prod_row":
        respo = get_prod_row(item=item)

    if item.command == "edit_prod_data":
        respo = edit_prod_data(item=item)

    if item.command == "list_prod_data":
        respo = list_prod_data(item=item)

    return respo

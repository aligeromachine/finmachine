from django.http import HttpRequest
import logging
from api.back.decore import validate_model
from api.back.products.model import ProductsMessage
from api.back.products.table import table_prod_data
from api.back.products.base import add_prod_data, delete_prod_row, edit_prod_data, get_prod_row, list_prod_data

logger = logging.getLogger(__name__)

@validate_model(ProductsMessage)  # type: ignore
def invoke_response(request: HttpRequest, item: ProductsMessage) -> dict:
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

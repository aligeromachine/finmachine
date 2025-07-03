from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.catalog.table import table_cat_data
from api.back.catalog.base import add_cat_data, delete_cat_row, edit_cat_data, get_cat_row, list_cat_data
from api.back.catalog.model import CatalogMessage

logger = logging.getLogger(__name__)

@validate_model(CatalogMessage)
def invoke_response(request: HttpRequest, item: CatalogMessage) -> dict:
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

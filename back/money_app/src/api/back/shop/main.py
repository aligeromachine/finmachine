from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.shop.model import ShopMessage
from api.back.shop.base import add_shop_data, delete_shop_row, edit_shop_data, get_shop_row, list_shop_data
from api.back.shop.table import table_shop_data

logger = logging.getLogger(__name__)

@validate_model(ShopMessage)
def invoke_response(request: HttpRequest, item: ShopMessage) -> dict:
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "table_shop_data":
        respo = table_shop_data(item=item)

    if item.command == "add_shop_data":
        respo = add_shop_data(item=item)

    if item.command == "delete_shop_row":
        respo = delete_shop_row(item=item)

    if item.command == "get_shop_row":
        respo = get_shop_row(item=item)

    if item.command == "edit_shop_data":
        respo = edit_shop_data(item=item)

    if item.command == "list_shop_data":
        respo = list_shop_data(item=item)

    return respo

from django.http import HttpRequest
from api.model.main import validate_model
from api.back.buy.table import table_buy_data
from api.back.buy.model import BuyMessage
from api.back.buy.base import add_buy_data, delete_buy_row, edit_buy_data, get_buy_row

@validate_model(BuyMessage)
def invoke_response(request: HttpRequest, item: BuyMessage) -> dict:
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "table_buy_data":
        respo = table_buy_data(item=item)

    if item.command == "add_buy_data":
        respo = add_buy_data(item=item)

    if item.command == "delete_buy_row":
        respo = delete_buy_row(item=item)

    if item.command == "get_buy_row":
        respo = get_buy_row(item=item)

    if item.command == "edit_buy_data":
        respo = edit_buy_data(item=item)

    return respo

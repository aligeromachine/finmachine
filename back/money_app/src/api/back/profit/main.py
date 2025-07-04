from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.profit.base import add_profit_data, delete_profit_row, edit_profit_data, get_profit_row
from api.back.profit.table import table_profit_data
from api.back.profit.model import ProfitMessage

logger = logging.getLogger(__name__)

@validate_model(ProfitMessage)
def invoke_response(request: HttpRequest, item: ProfitMessage) -> dict:
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "table_profit_data":
        respo = table_profit_data(item=item)

    if item.command == "add_profit_data":
        respo = add_profit_data(item=item)

    if item.command == "delete_profit_row":
        respo = delete_profit_row(item=item)

    if item.command == "get_profit_row":
        respo = get_profit_row(item=item)

    if item.command == "edit_profit_data":
        respo = edit_profit_data(item=item)

    return respo

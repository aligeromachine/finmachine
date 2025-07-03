from django.http import HttpRequest
from api.model.main import validate_model
from api.back.cards.model import CardsMessage
from api.back.cards.table import table_cards_data
from api.back.cards.base import add_cards_data, delete_cards_row, edit_cards_data, get_cards_row

@validate_model(CardsMessage)
def invoke_response(request: HttpRequest, item: CardsMessage) -> dict:
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "table_cards_data":
        respo = table_cards_data(item=item)

    if item.command == "add_cards_data":
        respo = add_cards_data(item=item)

    if item.command == "delete_cards_row":
        respo = delete_cards_row(item=item)

    if item.command == "get_cards_row":
        respo = get_cards_row(item=item)

    if item.command == "edit_cards_data":
        respo = edit_cards_data(item=item)

    return respo

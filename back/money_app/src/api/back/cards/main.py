from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.decore import draw_response
from money.utils.func import model_max_id
from money.libs.ext_utils import timeDRFF
from money.models import Cards
from api.model.cards import CardsMessage
from api.back.cards.query import SQL_CARDS, CARDS_TOTAL

logger = logging.getLogger(__name__)

@draw_response
def table_cards_data(item: CardsMessage):
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = []
    for it in Cards.objects.raw(raw_query=SQL_CARDS, params=params):
        raw = {
            'id': it.id,
            'created': timeDRFF(it.created),
            'title': it.title,
            'amount': it.amount,
            'number': it.number,
        }
        ls.append(raw)

    params = [item.user_id]
    count: int = 0
    for it in Cards.objects.raw(raw_query=CARDS_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

def add_cards_data(item: CardsMessage):
    Cards(
        title=item.title, 
        amount=item.amount,
        number=item.number,
        user_id=item.user_id
    ).save()
    max_id = model_max_id(model=Cards)

    return {'data': 'ok', 'message': f'adding shop key: {max_id}'}

def delete_cards_row(item: CardsMessage):
    Cards.objects.filter(pk=item.pk).delete()
    return {'data': 'ok', 'message': f'delete shop key: {item.pk}'}

def get_cards_row(item: CardsMessage):
    data = {}

    for it in Cards.objects.filter(pk=item.pk):
        data["title"] = it.title
        data["amount"] = it.amount
        data["number"] = it.number

    return data

def edit_cards_data(item: CardsMessage):
    try:
        instance = Cards.objects.get(pk=item.pk)

        instance.title = item.title
        instance.amount = item.amount
        instance.number = item.number
        instance.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}


@validate_model(CardsMessage)
def invoke_response(request: HttpRequest, item: CardsMessage):
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

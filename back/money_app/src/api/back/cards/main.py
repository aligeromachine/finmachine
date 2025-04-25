from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.decore import draw_response
from money.libs.ext_utils import timeDRFF
from money.models import Cards
from api.model.cards import CardsMessage
from api.back.cards.query import SQL_CARDS, CARDS_TOTAL

logger = logging.getLogger(__name__)

@draw_response
def update_cards_data(item: CardsMessage):
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

@validate_model(CardsMessage)
def invoke_response(request: HttpRequest, item: CardsMessage):
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "update_cards_data":
        respo = update_cards_data(item=item)

    return respo

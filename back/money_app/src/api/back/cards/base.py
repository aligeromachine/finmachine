import logging
from api.back.cards.model import CardSignal, CardsMessage
from money.utils.func import model_max_id
from money.models import Cards

logger = logging.getLogger(__name__)

def add_cards_data(item: CardsMessage) -> dict:
    Cards(
        title=item.title,
        amount=item.amount,
        number=item.number,
        user_id=item.user_id
    ).save()
    max_id = model_max_id(model=Cards)

    return {'data': 'ok', 'message': f'adding shop key: {max_id}'}

def delete_cards_row(item: CardsMessage) -> dict:
    Cards.objects.filter(pk=item.pk).delete()
    return {'data': 'ok', 'message': f'delete shop key: {item.pk}'}

def get_cards_row(item: CardsMessage) -> dict:
    data: dict = {}
    for it in Cards.objects.filter(pk=item.pk):
        data = CardSignal.from_orm(it).model_dump()
    return data

def edit_cards_data(item: CardsMessage) -> dict:
    try:
        instance = Cards.objects.get(pk=item.pk)

        instance.title = item.title
        instance.amount = item.amount
        instance.number = item.number
        instance.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}

import logging
from api.back.profit.model import ProfitMessage, ProfitSignal
from money.models import Profit

logger = logging.getLogger(__name__)

def add_profit_data(item: ProfitMessage) -> dict:
    elem = Profit.objects.create(title=item.title, amount=item.amount, source_id=item.source, user_id=item.user_id)
    elem.created = item.created
    elem.save()
    return {'data': 'ok', 'message': f'adding Profit key: {elem.pk}'}

def delete_profit_row(item: ProfitMessage) -> dict:
    Profit.objects.filter(pk=item.pk).delete()
    return {'data': 'ok', 'message': f'delete Profit key: {item.pk}'}

def get_profit_row(item: ProfitMessage) -> dict:
    data: dict = {}
    for it in Profit.objects.filter(pk=item.pk):
        data = ProfitSignal.from_orm(it).model_dump()
    return data

def edit_profit_data(item: ProfitMessage) -> dict:
    try:
        elem = Profit.objects.get(pk=item.pk)

        elem.title = item.title
        elem.amount = item.amount
        elem.source_id = item.source
        elem.created = item.created
        elem.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}

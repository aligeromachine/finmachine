import logging
from api.back.buy.model import BuyMessage, BuySignal
from machine.shift.model.buy import MacBuyShift
from money.models import Buy
from api.back.buy.query import BUY_ROW

logger = logging.getLogger(__name__)

@MacBuyShift.row_change  # type: ignore
def add_buy_data(item: BuyMessage) -> dict:
    elem = Buy.objects.create(title=item.title, amount=item.amount, shop_id=item.shop, products_id=item.prod, user_id=item.user_id)
    elem.created = item.created
    elem.save()
    return {'data': 'ok', 'message': f'adding Buy key: {elem.pk}'}

@MacBuyShift.row_change  # type: ignore
def delete_buy_row(item: BuyMessage) -> dict:
    Buy.objects.filter(pk=item.pk).delete()
    return {'data': 'ok', 'message': f'delete Buy key: {item.pk}'}

@MacBuyShift.row_save_redis  # type: ignore
def get_buy_row(item: BuyMessage) -> dict:
    data: dict = {}
    for it in Buy.objects.raw(raw_query=BUY_ROW, params=[item.pk]):
        data = BuySignal.from_orm(it).model_dump()
    return data

@MacBuyShift.row_edit  # type: ignore
def edit_buy_data(item: BuyMessage) -> dict:
    try:
        elem = Buy.objects.get(pk=item.pk)

        elem.title = item.title
        elem.amount = item.amount
        elem.shop_id = item.shop
        elem.products_id = item.prod
        elem.created = item.created
        elem.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}

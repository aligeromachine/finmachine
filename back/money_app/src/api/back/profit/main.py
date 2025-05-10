from django.http import HttpRequest
import logging
from api.model.main import validate_model
from api.back.decore import draw_response
from money.utils.func import model_max_id
from money.libs.ext_utils import timeDRFF
from money.models import Profit
from api.model.profit import ProfitMessage
from api.back.profit.query import SQL_PROFIT, PROFIT_TOTAL

logger = logging.getLogger(__name__)

@draw_response
def table_profit_data(item: ProfitMessage):
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = []
    for it in Profit.objects.raw(raw_query=SQL_PROFIT, params=params):
        raw = {
            'id': it.id,
            'created': timeDRFF(it.created),
            'title': it.title,
            'sources': it.sources,
        }
        ls.append(raw)

    params = [item.user_id]
    count: int = 0
    for it in Profit.objects.raw(raw_query=PROFIT_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit

def add_profit_data(item: ProfitMessage):
    Profit(title=item.title, user_id=item.user_id).save()
    max_id = model_max_id(model=Profit)

    return {'data': 'ok', 'message': f'adding Profit key: {max_id}'}

def delete_profit_row(item: ProfitMessage):
    Profit.objects.filter(pk=item.pk).delete()
    return {'data': 'ok', 'message': f'delete Profit key: {item.pk}'}

def get_profit_row(item: ProfitMessage):
    data = {}

    for it in Profit.objects.filter(pk=item.pk):
        data["title"] = it.title

    return data

def edit_profit_data(item: ProfitMessage):
    try:
        instance = Profit.objects.get(pk=item.pk)

        instance.title = item.title
        instance.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}

@validate_model(ProfitMessage)
def invoke_response(request: HttpRequest, item: ProfitMessage):
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

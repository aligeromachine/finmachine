from datetime import datetime
from money.ext_func.ext_c import CONST
from money.ext_func.ext_utils import reder_csv
from money.back.dash.model import Trati
from django.http import HttpRequest
import logging
from decimal import Decimal

from money.models import Transaction
from money.back.func import get_raw_path
from money.back.models import DashboardMessage, parse_model

logger = logging.getLogger(__name__)


def update_money_csv(item: DashboardMessage):
    respo = {"data": "ok", "message": "update_money_csv"}
    
    def GetAddressWatchService():
        
        from django.contrib.auth.models import User
        user = User.objects.get(pk=1)

        nfile = f'{get_raw_path()}/trati.csv'
        elastic_data = [Trati(*it) for it in reder_csv(nfile)]

        for chunk in elastic_data:
            logger.info(chunk)
            amount = Decimal(chunk.cena_tr)
            Transaction(
                title=chunk.prim_tr,
                amount=amount,
                store_id=chunk.kod_org_tr,
                products_id=chunk.kod_prod_tr,
                user=user
            ).save()

            pk: int = Transaction.objects.last().pk
            dt: datetime = datetime.strptime(chunk.data_tr, CONST.FormatAccess)

            Transaction.objects.filter(pk=pk).update(created=dt)

    import threading
    threading.Thread(target=GetAddressWatchService, args=()).start()

    return respo

@parse_model(DashboardMessage)
def invoke_response(request: HttpRequest, item: DashboardMessage):
    respo = {"data": "err", "message": "undefinded"}
    
    if item.command == "update_money_csv":
        respo = update_money_csv(item=item)
    
    return respo

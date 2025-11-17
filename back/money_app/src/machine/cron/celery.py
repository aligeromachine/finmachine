import logging
from machine.cron.query import GROUP_USER_YEAR_BUY_PROFIT
from money.models import Buy, AuditFin
from machine.cron.model import FinStat

logger = logging.getLogger(__name__)

def machine_audit() -> None:

    ls: list[FinStat] = [FinStat.from_orm(it) for it in Buy.objects.raw(raw_query=GROUP_USER_YEAR_BUY_PROFIT)]
    for it in ls:

        if not it.payload:
            continue

        elem, created = AuditFin.objects.get_or_create(user_id=it.user_id)
        elem.payload = [mx.model_dump() for mx in it.payload]
        elem.save()

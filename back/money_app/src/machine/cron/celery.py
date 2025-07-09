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

        if not AuditFin.objects.filter(user_id=it.user_id).count():
            AuditFin.objects.create(
                user_id=it.user_id,
                payload=[mx.model_dump() for mx in it.payload]
            )
        else:
            AuditFin.objects.filter(user_id=it.user_id).update(payload=[mx.model_dump(exclude={"delta"}) for mx in it.payload])

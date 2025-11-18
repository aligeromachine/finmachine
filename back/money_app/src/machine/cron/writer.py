from machine.tools.model import FinStat
from money.models import AuditFin

def write_payload(it: FinStat) -> None:
    elem, created = AuditFin.objects.get_or_create(user_id=it.user_id)
    elem.payload = [mx.model_dump() for mx in it.payload]
    elem.save()

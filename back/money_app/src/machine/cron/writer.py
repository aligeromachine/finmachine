from machine.tools.converter import to_payload
from machine.tools.model import FinStat
from money.models import AuditFin

def write_payload(it: FinStat) -> None:
    elem, created = AuditFin.objects.get_or_create(user_id=it.user_id)
    elem.payload = [it.model_dump() for it in to_payload(it.payload)]
    elem.save()

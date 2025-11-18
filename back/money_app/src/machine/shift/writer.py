from machine.tools.model import WidgetRange
from money.models import AuditFin

def rewrite_payload(user_id: int, rng: list[WidgetRange]) -> None:
    elem = AuditFin.objects.get(user_id=user_id)
    elem.payload = [mx.model_dump() for mx in rng]
    elem.save()

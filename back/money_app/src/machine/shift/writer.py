from machine.tools.converter import to_payload
from machine.tools.model import WidgetRange
from money.models import AuditFin

def rewrite_payload(user_id: int, rng: list[WidgetRange]) -> None:
    elem = AuditFin.objects.get(user_id=user_id)
    elem.payload = [it.model_dump() for it in to_payload(rng)]
    elem.save()

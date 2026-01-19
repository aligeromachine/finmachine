import logging
from machine.tools.converter import to_payload
from machine.tools.model import WidgetRange
from money.models import AuditFin

logger = logging.getLogger(__name__)

def rewrite_payload(user_id: int, rng: list[WidgetRange]) -> None:
    elem = None
    for raw in AuditFin.objects.filter(user_id=user_id):
        elem = AuditFin.objects.get(pk=raw.pk)
    
    if not elem:
        elem = AuditFin.objects.create(user_id=user_id)

    elem.payload = [it.model_dump() for it in to_payload(rng)]
    elem.save()

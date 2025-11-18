import logging
from machine.cron.writer import write_payload
from machine.tools.model import FinStat
from machine.tools.selector import list_audit

logger = logging.getLogger(__name__)

def machine_audit() -> None:

    ls: list[FinStat] = list_audit()
    for it in ls:

        if not it.payload:
            continue

        write_payload(it=it)

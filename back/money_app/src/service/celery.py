import os
from typing import Any
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings")
app = Celery("service")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.on_after_configure.connect  # type: ignore
def setup_periodic_tasks(sender: Any, **kwargs: Any) -> None:

    sender.add_periodic_task(
        crontab(minute=30, hour=8), # Каждый день в 8:30 утра
        moneyAudit, name='moneyAudit')
    
@app.task  # type: ignore
def moneyAudit() -> None:
    from machine.cron.celery import machine_audit
    machine_audit()

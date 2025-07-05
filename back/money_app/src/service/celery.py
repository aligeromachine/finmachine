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
        crontab(hour=0, minute=0, day_of_month=1, month_of_year=1),
        aggregation, name='aggregation')

@app.task  # type: ignore
def aggregation() -> None:
    from machine.cron.celery import machine_aggregation
    machine_aggregation()

import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings")
app = Celery("service")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(
        crontab(hour=0, minute=0, day_of_month=1, month_of_year=1),
        FinalizeYear,
        name='DeleteArhivExport')

@app.task
def FinalizeYear():
    pass

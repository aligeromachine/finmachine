import logging
import os
import re
from money.libs.ext_utils import (
    AbsPath,
    CreateDirectory)
from service.settings import MEDIA_ROOT
from datetime import datetime, timedelta
from money.libs.ext_c import (
    CONST,
    PathNames)
from django.db import models
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

def create_task_dir(name: str, dt: datetime) -> str:
    folder = CreateDirectory(a=MEDIA_ROOT, b=name)
    folder = CreateDirectory(a=folder, b=dt.strftime('%Y'))
    folder = CreateDirectory(a=folder, b=dt.strftime('%m'))
    folder = CreateDirectory(a=folder, b=dt.strftime('%d'))

    return str(folder)

def put_file_base(nf: str, dt: datetime, prefix: str) -> str:
    drv: str = CONST.empty

    if not dt:
        return drv
    if nf in CONST.emptyls:
        return drv

    folder = create_task_dir(name=prefix, dt=dt)
    file_path: str = AbsPath(folder, nf)

    return file_path

def get_file_base(nf: str, dt: datetime, prefix: str) -> str:
    drv: str = CONST.empty

    if not dt:
        return drv
    if nf in CONST.emptyls:
        return drv

    return str(AbsPath(MEDIA_ROOT, prefix, dt.strftime('%Y'), dt.strftime('%m'), dt.strftime('%d'), nf))

def get_base_crusher(name: str) -> str:

    folder = AbsPath(MEDIA_ROOT, PathNames.crusher)
    if not os.path.exists(folder):
        os.mkdir(folder)

    return str(AbsPath(folder, name))

def get_raw_path() -> str:

    folder = AbsPath(MEDIA_ROOT, PathNames.raw)
    if not os.path.exists(folder):
        os.mkdir(folder)

    return str(AbsPath(folder))

def RULES_ROUTE(user: str) -> list:
    for it in User.objects.filter(username=user):
        return str(it.last_name).split(',')
    return []

def is_super_user(user: str) -> bool:
    for it in User.objects.filter(username=user):
        return bool(it.is_superuser)
    return False

def UpdateSQl(query: str, values: list) -> None:
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(query, values)

def date_to_tuple_tasks(dt: str) -> tuple:

    if dt == CONST.empty:
        return None, None, False

    dt_arr = dt.split('to')
    begin = dt_arr[0].strip()

    if len(dt_arr) == 1:
        return begin, begin, True

    end = dt_arr[1].strip()

    return begin, end, True

def date_to_tuple_dashboard(dt: str, context: dict) -> tuple:
    begin = context["begin"]
    end = context["end"]

    if dt == CONST.empty:
        return begin, end

    dt_arr = dt.split('to')

    if len(dt_arr) == 1:
        return begin, begin

    begin = dt_arr[0].strip()
    end = dt_arr[1].strip()

    return begin, end

def daterange(begin: str, end: str) -> list:
    date1 = datetime.strptime(begin, '%Y-%m-%d')
    date2 = datetime.strptime(end, '%Y-%m-%d')
    return [(date1 + timedelta(days=x)).strftime(CONST.FDate) for x in range((date2 - date1).days + 1)]

def CreateWorkDir(dt: datetime, name: str) -> str:
    folder = CreateDirectory(a=MEDIA_ROOT, b=name)
    folder = CreateDirectory(a=folder, b=dt.strftime('%Y'))
    folder = CreateDirectory(a=folder, b=dt.strftime('%m'))
    folder = CreateDirectory(a=folder, b=dt.strftime('%d'))

    return str(folder)

def GetResultFolder() -> str:
    return str(AbsPath(MEDIA_ROOT, PathNames.exchange))

def serializing_dt_str(name: str) -> datetime | None:
    match = re.search(r"(\d+)-(\d+)-(\d+)_(\d+)-(\d+)-(\d+)", name)

    if not match:
        return None

    year = int(match.group(3))
    month = int(match.group(2))
    day = int(match.group(1))
    hour = int(match.group(4))
    minute = int(match.group(5))
    second = int(match.group(6))
    dt: datetime = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)

    return dt

def PutDTResult(name: str) -> str | None:
    dt = serializing_dt_str(name)
    if not dt:
        return None
    folder = CreateWorkDir(dt=dt, name=PathNames.exchange)

    return str(AbsPath(folder, name))

def GetDTResult(name: str) -> str | None:
    dt = serializing_dt_str(name)
    if not dt:
        return None

    return str(AbsPath(MEDIA_ROOT, PathNames.exchange, dt.strftime('%Y'), dt.strftime('%m'), dt.strftime('%d'), name))

def model_max_id(model: models.Model) -> int:
    max_id = model.objects.last()
    return int(max_id.pk)

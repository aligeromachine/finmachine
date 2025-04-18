from datetime import datetime, timedelta
from django.db import models
from functools import wraps
import os
import re
import time
import orjson
from money.ext_func.ext_utils import AbsPath, CreateDirectory, DaysDeltaNow, RandomName, ReadFileContent
from money.ext_func.ext_c import CONST, PathNames
from django.contrib.auth.models import User
import logging

from service.settings import MEDIA_ROOT


logger = logging.getLogger(__name__)

remove_spec = lambda x: re.sub(r"['\" ]", "", x)


def RULES_ROUTE(user: str):
    for it in User.objects.filter(username=user):
        return str(it.last_name).split(',')
    
    return []

def is_super_user(user: str):
    
    for it in User.objects.filter(username=user):
        return it.is_superuser
    
    return False

def calculate_running_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        begin = time.time()
        
        random_name = RandomName(5).lower()

        result = func(random_name, *args, **kwargs)
        end = time.time()

        elapsed = end - begin
        elapsed_min = int(elapsed // 60)
        elapsed_sec = int(elapsed % 60)

        logger.info(f"{random_name} Время выполнения {func.__name__} {elapsed_min} минут {elapsed_sec} секунд.")

        return result
    return wrapper

def UpdateSQl(query: str, values: list):
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(query, values)

def date_to_tuple_tasks(dt: str):

    if dt == CONST.empty:
        return None, None, False

    dt_arr = dt.split('to')
    begin = dt_arr[0].strip()

    if len(dt_arr) == 1:
        return begin, begin, True
    
    end = dt_arr[1].strip()

    return begin, end, True

def date_to_tuple_dashboard(dt: str, context: dict):
    
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

def daterange(begin: str, end: str):
    date1 = datetime.strptime(begin, '%Y-%m-%d')
    date2 = datetime.strptime(end, '%Y-%m-%d')
    return [(date1 + timedelta(days=x)).strftime(CONST.FDate) for x in range((date2 - date1).days + 1)]

def context_date_range(begin: int = 7, end: int = 0):
    context = {
        'begin': DaysDeltaNow(begin).strftime(CONST.FDate),
        'end': DaysDeltaNow(end).strftime(CONST.FDate),
    }

    return context

def parse_date(dt: str, context: dict = context_date_range()):

    begin, end = date_to_tuple_dashboard(dt=dt, context=context)

    return f" BETWEEN '{begin} {CONST.DAY_BEGIN}' AND '{end} {CONST.DAY_END}' "


def CreateWorkDir(dt: datetime, name: str):
    folder = CreateDirectory(a=MEDIA_ROOT, b=name)
    folder = CreateDirectory(a=folder, b=dt.strftime('%Y'))
    folder = CreateDirectory(a=folder, b=dt.strftime('%m'))
    folder = CreateDirectory(a=folder, b=dt.strftime('%d'))

    return folder


def GetResultFolder():
    
    return AbsPath(MEDIA_ROOT, PathNames.exchange)

def MakeExhangeFolder():
    
    return CreateDirectory(a=MEDIA_ROOT, b=PathNames.exchange)

def serializing_dt_str(name: str):
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

def PutDTResult(name: str):
    
    dt = serializing_dt_str(name)
    if not dt:
        return None
    
    folder = CreateWorkDir(dt=dt, name=PathNames.exchange)

    return str(AbsPath(folder, name))
        

def GetDTResult(name: str):

    dt = serializing_dt_str(name)
    if not dt:
        return None
    
    return str(AbsPath(MEDIA_ROOT, PathNames.exchange, dt.strftime('%Y'), dt.strftime('%m'), dt.strftime('%d'), name))


def get_task_id_from_report(fname: str):
    
    raw_payload = os.path.basename(fname)
    ls_raw = raw_payload.split('_')

    if not ls_raw:
        return None
    
    if not len(ls_raw) == 3:
        return None

    task_id = ls_raw[0]

    return task_id


def model_max_id(model: models.Model):
    max_id = model.objects.last()
    return max_id.pk

auto_code_type_mac: dict | None = None

def auto_for_type_code(type_code: str):
    
    if not globals()['auto_code_type_mac']:
        fname = AbsPath(MEDIA_ROOT, PathNames.auto, "code.json")
        globals()['auto_code_type_mac'] = dict(orjson.loads(ReadFileContent(fname)))

    auto_code = globals()['auto_code_type_mac']
    
    key: str | None = None

    for k, v in dict(auto_code).items():
        
        ls = [str(it) for it in v]
        
        if type_code in ls:
            key = k
            break
    
    return key 

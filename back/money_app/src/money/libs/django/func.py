import os
import logging
from service.settings import MEDIA_ROOT
from datetime import datetime
from money.libs.const import CONST
from money.libs.files.exp import create_directory
from money.libs.dt.utils import pretty_Range_rev, time_name
from money.libs.files.base import abs_path, name_file

logger = logging.getLogger(__name__)

def create_task_dir(name: str, dt: datetime) -> str:
    folder = create_directory(a=MEDIA_ROOT, b=name)
    folder = create_directory(a=folder, b=dt.strftime('%Y'))
    folder = create_directory(a=folder, b=dt.strftime('%m'))
    folder = create_directory(a=folder, b=dt.strftime('%d'))

    return str(folder)

def put_file_base(nf: str, dt: datetime, prefix: str) -> str:
    rv_def: str = CONST.empty

    if not dt:
        return rv_def

    if nf in CONST.emptyls:
        return rv_def

    folder = create_task_dir(name=prefix, dt=dt)

    file_path: str = abs_path(folder, nf)

    return file_path

def get_file_base(nf: str, dt: datetime, prefix: str) -> str:
    rv_def: str = CONST.empty
    if not dt:
        return rv_def

    if nf in CONST.emptyls:
        return rv_def

    rv: str = abs_path(MEDIA_ROOT, prefix, dt.strftime('%Y'), dt.strftime('%m'), dt.strftime('%d'), nf)
    return rv

def _get_file_href_base(nf: str, dt: datetime, prefix: str) -> str:

    return get_file_base(nf=nf, dt=dt, prefix=prefix).replace(MEDIA_ROOT, '')

def get_raw_path() -> str:
    rv: str = create_directory(a=MEDIA_ROOT, b=CONST.raw)    
    return rv

def context_range_day() -> dict:
    rv: dict = pretty_Range_rev(begin=1, end=0)
    return rv

def context_range_week() -> dict:
    rv: dict = pretty_Range_rev(begin=7, end=0)
    return rv

def context_range_start_surok() -> dict:
    d0 = datetime.now()
    d1 = datetime(2018, 1, 1)
    delta = d0 - d1
    rv: dict = pretty_Range_rev(begin=delta.days, end=0)
    return rv

def context_range_year() -> dict:
    d0 = datetime.now()
    d1 = datetime(d0.year, 1, 1)
    delta = d0 - d1
    rv: dict = pretty_Range_rev(begin=delta.days, end=0)
    return rv

def context_range_month() -> dict:
    rv: dict = pretty_Range_rev(begin=31, end=0)
    return rv

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

def parse_date(dt: str, context: dict = pretty_Range_rev(begin=7, end=0)) -> str:
    begin, end = date_to_tuple_dashboard(dt=dt, context=context)
    return f" BETWEEN '{begin} {CONST.DAY_BEGIN}' AND '{end} {CONST.DAY_END}' "

def get_task_id_from_report(fname: str) -> str | None:
    raw_payload = name_file(fname)
    ls_raw = raw_payload.split('_')

    if not ls_raw:
        return None

    if not len(ls_raw) == 3:
        return None

    task_id: str = ls_raw[0]

    return task_id

from datetime import datetime
from money.ext_func.ext_utils import DaysDeltaNow
from money.ext_func.ext_c import CONST

def context_date_range(begin: int = 7, end: int = 0):
    context = {
        'begin': DaysDeltaNow(begin).strftime(CONST.FDate),
        'end': DaysDeltaNow(end).strftime(CONST.FDate),
    }

    return context

def context_range_day():
    return context_date_range(begin=1, end=0)

def context_range_week():
    return context_date_range(begin=7, end=0)

def context_range_start_money():
    d0 = datetime.now()
    d1 = datetime(2018, 1, 1)
    delta = d0 - d1
    return context_date_range(begin=delta.days, end=0)

def context_range_year():
    d0 = datetime.now()
    d1 = datetime(d0.year, 1, 1)
    delta = d0 - d1
    return context_date_range(begin=delta.days, end=0)

def context_range_month():
    return context_date_range(begin=31, end=0)

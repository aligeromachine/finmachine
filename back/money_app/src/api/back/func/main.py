from datetime import datetime
from libs.dt.utils import pretty_Range_rev

def context_range_day() -> dict[str, str]:
    rv: dict[str, str] = pretty_Range_rev(begin=1, end=0)
    return rv

def context_range_week() -> dict[str, str]:
    rv: dict[str, str] = pretty_Range_rev(begin=7, end=0)
    return rv

def context_range_start_money() -> dict[str, str]:
    d0 = datetime.now()
    d1 = datetime(2018, 1, 1)
    delta = d0 - d1
    rv: dict[str, str] = pretty_Range_rev(begin=delta.days, end=0)
    return rv

def context_range_year() -> dict[str, str]:
    d0 = datetime.now()
    d1 = datetime(d0.year, 1, 1)
    delta = d0 - d1
    rv: dict[str, str] = pretty_Range_rev(begin=delta.days, end=0)
    return rv

def context_range_month() -> dict[str, str]:
    rv: dict[str, str] = pretty_Range_rev(begin=31, end=0)
    return rv

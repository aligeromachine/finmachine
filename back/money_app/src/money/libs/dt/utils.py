from datetime import datetime, timedelta
from money.libs.dt.model import DateParser
from money.libs.const import CONST

def time_durations(begin: str, end: str) -> str:
    begin_t = DateParser.load_str(raw=begin)
    end_t = DateParser.load_str(raw=end)

    if not (begin_t and end_t):
        return str(CONST.empty)

    elapsed = (end_t.to_dt() - begin_t.to_dt()).total_seconds()
    emin = int(elapsed // 60)
    esec = int(elapsed % 60)

    return f"{emin} min, {esec} sec"

def pretty_str(raw: str | datetime) -> str:
    dt = DateParser.load_str(raw=raw) if isinstance(raw, str) else DateParser.load_dt(raw=raw)
    result: str = dt.pretty() if dt else CONST.empty
    return result

def pretty_short() -> str:
    result: str = DateParser.load_now().pretty_short(hours=3)
    return result

def pretty_shortX() -> str:
    result: str = DateParser.load_now().pretty_shortX(hours=3)
    return result

def pretty_base() -> str:
    result: str = DateParser.load_now().pretty(hours=3)
    return result

def timeF() -> str:
    result: str = DateParser.load_now().pretty_F(hours=3)
    return result

def timeDelta(hours: int = 3) -> datetime:
    dt: datetime = DateParser.load_now().time_Hours(hours=hours)
    return dt

def time_parse(raw: str | datetime) -> datetime | None:
    dt = DateParser.load_str(raw=raw) if isinstance(raw, str) else DateParser.load_dt(raw=raw)
    return dt.to_dt() if dt else None

def time_name(raw: str) -> datetime | None:
    dt = DateParser.load_name(raw=raw)
    return dt.to_dt() if dt else None

def pretty_Range_rev(begin: int, end: int) -> dict[str, str]:
    dt_begin = DateParser.load_now().pretty_short_rev(days=begin)
    dt_end = DateParser.load_now().pretty_short_rev(days=end)
    return dict(begin=dt_begin, end=dt_end)

def daterange(begin: str, end: str) -> list:
    date1 = datetime.strptime(begin, '%Y-%m-%d')
    date2 = datetime.strptime(end, '%Y-%m-%d')
    return [(date1 + timedelta(days=x)).strftime(CONST.FDate) for x in range((date2 - date1).days + 1)]

def timeDeltaMin(minutes: int = 0) -> datetime:
    dt: datetime = DateParser.load_now().time_Hours(hours=3, minutes=minutes)
    return dt

def timeDeltaDayRev(days: int = 0) -> datetime:
    dt: datetime = DateParser.load_now().to_dt_rev(days=days)
    return dt

def isDevideFive() -> bool:
    dt: datetime = DateParser.load_now()
    return dt.second % 5 == 0

from datetime import datetime, timedelta
import re
from typing import TypeVar
from pydantic import BaseModel
from money.libs.const import CONST


T = TypeVar('T', bound='DateParser')

class DateParser(BaseModel):
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int

    @classmethod
    def load_str(cls: type[T], raw: str) -> T | None:
        if not raw:
            return None

        p1 = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})(T| )(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})"
        p2 = r"(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})(T| )(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})"
        for it in [p1, p2]:
            match = re.search(it, raw)
            if match:
                data: dict[str, int] = {k: int(v) for k, v in match.groupdict().items()}
                return cls(**data)

        return None

    @classmethod
    def load_name(cls: type[T], raw: str) -> T | None:
        if not raw:
            return None

        p1 = r"(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})_(?P<hour>\d{2})-(?P<minute>\d{2})-(?P<second>\d{2})"
        p2 = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})_(?P<hour>\d{2})-(?P<minute>\d{2})-(?P<second>\d{2})"
        for it in [p1, p2]:
            match = re.search(it, raw)
            if match:
                data: dict[str, int] = {k: int(v) for k, v in match.groupdict().items()}
                return cls(**data)

        return None

    @classmethod
    def load_dt(cls: type[T], raw: datetime) -> T | None:
        if not raw:
            return None

        return cls(**dict(year=raw.year, month=raw.month, day=raw.day, hour=raw.hour, minute=raw.minute, second=raw.second))

    @classmethod
    def load_now(cls: type[T]) -> T:
        nw = datetime.now() 
        return cls(**dict(year=nw.year, month=nw.month, day=nw.day, hour=nw.hour, minute=nw.minute, second=nw.second))

    def calc(self, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0) -> tuple[datetime, timedelta]:
        dt = datetime(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute, second=self.second)
        delta = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        return dt, delta

    def to_dt(self, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0) -> datetime:
        dt, delta = self.calc(days, hours, minutes, seconds)
        return dt + delta

    def to_dt_rev(self, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0) -> datetime:
        dt, delta = self.calc(days, hours, minutes, seconds)
        return dt - delta

    def pretty(self, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0) -> str:
        return self.to_dt(days, hours, minutes, seconds).strftime(CONST.FormatT)

    def pretty_db(self, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0) -> str:
        return self.to_dt(days, hours, minutes, seconds).strftime(CONST.FormatDDP)

    def pretty_short(self, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0) -> str:
        return self.to_dt(days, hours, minutes, seconds).strftime(CONST.FDate)

    def pretty_short_rev(self, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0) -> str:
        return self.to_dt_rev(days, hours, minutes, seconds).strftime(CONST.FDate)

    def pretty_F(self, hours: int = 3) -> str:
        return self.to_dt(hours=hours).strftime(CONST.FormatF)

    def pretty_shortX(self, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0) -> str:
        return self.to_dt(days, hours, minutes, seconds).strftime(CONST.FTime)

    def time_Hours(self, hours: int = 0, minutes: int = 0) -> datetime:
        return self.to_dt(hours=hours, minutes=minutes)

    def time_Days(self, days: int = 0) -> datetime:
        return self.to_dt(days=days)

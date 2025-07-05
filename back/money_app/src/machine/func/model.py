from typing import Self
from pydantic import BaseModel

class AggInfo(BaseModel):

    @classmethod
    def load_from_db(cls) -> "AggInfo":
        g = globals()

        if 'speed_in_redis' not in g:
            g['speed_in_redis'] = speed_mac_selector()

        raw_speed: list[SpeedMacSelector] = g['speed_in_redis']  # type ignore
        return raw_speed

    @classmethod
    def get_selector(cls, machine: str) -> list[str]:
        raw_speed: list[SpeedMacSelector] = cls.get_speed()

        selector: list[str] = []

        for it in raw_speed:
            if machine == it.machine:
                selector.extend(it.hashtypes)

        selector = sorted(selector, key=lambda x: int(x))

        return selector

    @classmethod
    def get_other_selector(cls, id: str) -> list[str]:
        raw_speed: list[SpeedMacSelector] = cls.get_speed()

        selector: list[str] = []

        for it in raw_speed:
            if id != it.id:
                selector.extend(it.hashtypes)

        selector = sorted(selector, key=lambda x: int(x))

        return selector

    @classmethod
    def get_mac(cls, hash_type: str) -> str:
        from machine.const.code import MAC_KEY
        raw_speed: list[SpeedMacSelector] = cls.get_speed()

        mac: str = ''
        for ix in raw_speed:
            if hash_type in ix.hashtypes:
                mac = MAC_KEY[ix.machine]

        return mac

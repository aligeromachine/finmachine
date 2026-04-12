from typing import TypeVar
from pydantic import BaseModel
from libs.files.exp import ClearFile
from libs.files.base import read_text_data
from libs.const import CONST
import logging

logger = logging.getLogger(__name__)

T = TypeVar('T', bound='MacResult')

def psw_convert(psw: str | None) -> str | None:
    if psw is None:
        return None
    hext: str = '$HEX'
    if psw.startswith(hext):
        return bytes.fromhex(psw.strip()[5:-1]).decode(encoding=CONST.UTF8, errors='ignore')

    return psw.strip()

class MacResult(BaseModel):
    hash: str = CONST.empty
    password: str | None = None

    @classmethod
    def load(cls: type[T], fname: str) -> T | None:
        pat: str = ':'
        response = read_text_data(pth=fname)
        ClearFile(pth=fname)

        match response.split(pat, 1):
            case [raw_hash, raw_password]:
                return cls(**dict(hash=raw_hash.strip(), password=psw_convert(raw_password)))

        return None

    def to_str(self) -> str:
        return f'{self.hash}:{self.password}'

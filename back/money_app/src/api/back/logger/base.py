import logging
import os
from api.back.logger.model import LOG_ALL, LOG_API, LOG_DJANGO, LOG_MONEY, LogAllSignal, LogMessage, LogSignal
from money.libs.ext_c import CONST
from money.libs.ext_utils import ClearFile, ReadFileContent

logger = logging.getLogger(__name__)

BASE_LOG: str = '/home/data/media/log'

logger = logging.getLogger(__name__)

def get_log(fname: str) -> str:
    rv: str = ReadFileContent(pth=fname) if os.path.isfile(fname) else CONST.empty
    return rv

def call_file(item: LogMessage, fcall: str) -> dict:
    fname = f'{BASE_LOG}/{fcall}.log'

    if item.command.startswith('delete'):
        ClearFile(pth=fname)

    return LogSignal(message=get_log(fname=fname)).model_dump()


def call_all() -> dict:

    data = LogAllSignal(
        money=get_log(fname=f'{BASE_LOG}/{LOG_MONEY}.log'),
        api=get_log(fname=f'{BASE_LOG}/{LOG_API}.log'),
        django=get_log(fname=f'{BASE_LOG}/{LOG_DJANGO}.log'),
    )
    return LogSignal(message=data.model_dump()).model_dump()

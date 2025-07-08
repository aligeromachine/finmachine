from django.http import HttpRequest
import logging
from api.back.decore import validate_model
from api.back.logger.model import LOG_ALL, LOG_API, LOG_DJANGO, LOG_MONEY, LogMessage
from api.back.logger.base import call_all, call_file

logger = logging.getLogger(__name__)

@validate_model(LogMessage)  # type: ignore
def invoke_response(request: HttpRequest, item: LogMessage) -> dict:
    respo = {"data": "err", "message": "undefinded"}

    if item.command.endswith(LOG_DJANGO):
        respo = call_file(item, LOG_DJANGO)

    if item.command.endswith(LOG_API):
        respo = call_file(item, LOG_API)

    if item.command.endswith(LOG_MONEY):
        respo = call_file(item, LOG_MONEY)
    
    if item.command == LOG_ALL:
        respo = call_all()

    return respo

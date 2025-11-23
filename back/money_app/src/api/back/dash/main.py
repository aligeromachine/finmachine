from api.back.dash.model import DashboardMessage
from django.http import HttpRequest
import logging
from api.back.decore import validate_model
from api.back.dash.base import base_info

logger = logging.getLogger(__name__)

@validate_model(DashboardMessage)  # type: ignore
def invoke_response(request: HttpRequest, item: DashboardMessage) -> dict:
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "base_info":
        respo = base_info(item=item)

    return respo

from django.http import HttpRequest
import logging
from api.back.decore import validate_model
from api.back.source.model import SourceMessage
from api.back.source.base import add_source_data, delete_source_row, edit_source_data, get_source_row, list_source_data
from api.back.source.table import table_source_data

logger = logging.getLogger(__name__)

@validate_model(SourceMessage)  # type: ignore
def invoke_response(request: HttpRequest, item: SourceMessage) -> dict:
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "table_source_data":
        respo = table_source_data(item=item)

    if item.command == "add_source_data":
        respo = add_source_data(item=item)

    if item.command == "delete_source_row":
        respo = delete_source_row(item=item)

    if item.command == "get_source_row":
        respo = get_source_row(item=item)

    if item.command == "edit_source_data":
        respo = edit_source_data(item=item)

    if item.command == "list_source_data":
        respo = list_source_data(item=item)

    return respo

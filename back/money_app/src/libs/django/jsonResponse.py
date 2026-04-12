from datetime import datetime
from typing import Any
import orjson
from django.http import HttpResponse
from pydantic import BaseModel

class ORJSONResponse(HttpResponse):
    def __init__(
            self, 
            data: dict | list | BaseModel, 
            status: int = 200, 
            safe: bool = True, 
            option: int | None = None, 
            content_type: str = 'application/json', 
            **kwargs: Any) -> None:

        if isinstance(data, BaseModel):
            data = data.model_dump()

        if safe and not (isinstance(data, dict) or isinstance(data, list)):
            raise TypeError(
                'In order to allow non-dict or non-list objects to be serialized set the '
                'safe parameter to False.'
            )

        # Настройки orjson по умолчанию
        if option is None:
            option = orjson.OPT_SERIALIZE_NUMPY | orjson.OPT_NAIVE_UTC

        # Сериализация
        content = orjson.dumps(data, default=self._default, option=option)

        super().__init__(
            content=content, 
            status=status, 
            content_type=content_type, 
            **kwargs
        )

    @staticmethod
    def _default(obj: Any) -> list | str | float:
        """Обработка специальных типов"""
        # Django модели
        if hasattr(obj, 'pk') and hasattr(obj, '__class__'):
            return str(obj)

        # Дата и время
        if hasattr(obj, 'isoformat'):
            if isinstance(obj, datetime):
                return obj.isoformat()

        # Decimal
        if hasattr(obj, 'quantize'):
            return float(obj)

        # UUID
        if hasattr(obj, 'hex'):
            return str(obj)

        # Множества и кортежи
        if isinstance(obj, (set, tuple)):
            return list(obj)

        raise TypeError(f'Object of type {type(obj)} is not JSON serializable')

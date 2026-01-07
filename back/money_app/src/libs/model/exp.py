from pydantic import BaseModel
from typing import Any, TypeVar

T = TypeVar('T', bound='BaseModelWithRawArray')

class BaseModelWithRawArray(BaseModel):
    """Базовый класс с поддержкой from_raw_query для наследования"""

    @classmethod
    def from_raw_array(cls: type[T], raw_item: Any) -> T:
        if isinstance(raw_item, list) or isinstance(raw_item, tuple):
            key: str = "properties"
            schema: dict = cls.model_json_schema()
            properties: dict = dict(schema[key]) if key in schema else {}
            field_order = [filed for filed, _ in properties.items()]
            return cls(**dict(zip(field_order, raw_item)))

        raise ValueError(f"Unsupported raw item type: {type(raw_item)}")

    @classmethod
    def from_raw_dict(cls: type[T], raw_item: dict) -> T:
        if isinstance(raw_item, dict):
            return cls(**raw_item)

        raise ValueError(f"Unsupported raw item type: {type(raw_item)}")

    @classmethod
    def from_orm(cls: type[T], raw_item: Any) -> T:
        # Если это объект ORM (например, Django или SQLAlchemy)

        # if hasattr(raw_item, '__dict__'):
        #     # Исключаем служебные атрибуты ORM
        #     data = {
        #         k: v for k, v in raw_item.__dict__.items()
        #         if not k.startswith('_')
        #     }
        #     return cls(**data)

        if hasattr(raw_item, '__dict__'):
            return cls(**raw_item.__dict__)

        raise ValueError(f"Unsupported raw item type: {type(raw_item)}")

    @classmethod
    def from_orm_index(cls: type[T], raw_item: Any, index: int) -> T:
        if hasattr(raw_item, '__dict__'):
            result = cls(**raw_item.__dict__)
            result.index = index  # type: ignore
            return result

        raise ValueError(f"Unsupported raw item type: {type(raw_item)}")

from pydantic import BaseModel
from typing import Any, TypeVar

T = TypeVar('T', bound='BaseModelWithRawQuery')

class BaseModelWithRawQuery(BaseModel):
    """Базовый класс с поддержкой from_raw_query для наследования"""

    @classmethod
    def from_raw_query(cls: type[T], raw_item: Any) -> T:
        """
        Преобразует сырые данные в модель, поддерживая наследование.
        Args:
            raw_item: Данные из БД (dict, ORM-объект и т.д.)
        Returns:
            Экземпляр модели (может быть подклассом)
        """
        if isinstance(raw_item, dict):
            return cls(**raw_item)

        # if hasattr(raw_item, '__dict__'):
        #     # Исключаем служебные атрибуты ORM
        #     data = {
        #         k: v for k, v in raw_item.__dict__.items()
        #         if not k.startswith('_')
        #     }
        #     return cls(**data)

        # Если это объект ORM (например, Django или SQLAlchemy)
        if hasattr(raw_item, '__dict__'):
            return cls(**raw_item.__dict__)

        raise ValueError(f"Unsupported raw item type: {type(raw_item)}")

    @classmethod
    def from_raw_queryset(cls: type[T], raw_items: list[Any]) -> list[T]:
        """Обрабатывает список сырых данных"""
        return [cls.from_raw_query(item) for item in raw_items]

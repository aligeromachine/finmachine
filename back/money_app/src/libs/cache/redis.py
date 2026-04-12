import logging
import redis
from typing import Self, Any
from libs.validate.exp import validate_conv, to_json

logger = logging.getLogger(__name__)

class RedisClient:

    def __init__(self, host: str, port: int, db: int) -> None:
        self.client = redis.Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True,
        )

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore
        self.client.close()  # type: ignore

    def __enter__(self) -> Self:
        return self

    def set_key(self, key: str, value: str) -> None:
        self.client.set(key, value)

    def get_key(self, key: str) -> Any:
        if self.exists_key(key=key):
            return self.client.get(key)
        return None

    def delete_key(self, key: str) -> bool:
        if self.exists_key(key=key):
            return bool(self.client.delete(key))
        return False

    def exists_key(self, key: str) -> bool:
        try:
            return bool(self.client.exists(key))
        except:  # noqa
            return False

    def set_key_json(self, key: str, value: list | dict) -> None:
        if isinstance(value, (dict, list)):
            self.set_key(key=key, value=to_json(data=value))

    def get_key_json(self, key: str) -> Any:
        value = self.get_key(key=key)
        if value:
            return validate_conv(value)
        return None

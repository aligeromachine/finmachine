import redis
from typing import Self, Any

class RedisStorage:

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore
        self.client.close()  # type: ignore

    def __enter__(self) -> Self:
        return self

    def __init__(self, host: str) -> None:

        self.client = redis.Redis(host=host, port=6379, db=0)

    def set(self, key: str, value: str) -> None:
        self.client.set(key, value)

    def get(self, key: str) -> Any:
        return self.client.get(key)

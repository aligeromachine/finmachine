import redis


class RedisStorage:

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def __enter__(self):
        return self

    def __init__(self, host: str) -> None:

        self.client = redis.Redis(host=host, port=6379, db=0)

    def set(self, key: str, value: str):
        return self.client.set(key, value)

    def get(self, key: str):
        return self.client.get(key)

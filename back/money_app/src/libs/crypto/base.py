import hashlib
from _hashlib import HASH


class SHABaseHasher:
    hash_object: HASH

    def __init__(self) -> None:
        self.reset()

    def update_str(self, raw: str) -> None:
        self.hash_object.update(raw.encode())

    def update_bytes(self, raw: bytes) -> None:
        self.hash_object.update(raw)

    def get_hash(self) -> str:
        return self.hash_object.hexdigest()

    def reset(self) -> None:
        pass

class SHA256Hasher(SHABaseHasher):
    def reset(self) -> None:
        self.hash_object = hashlib.sha256()

class MD5Hasher(SHABaseHasher):
    def reset(self) -> None:
        self.hash_object = hashlib.md5()

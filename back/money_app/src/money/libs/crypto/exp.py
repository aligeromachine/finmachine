from money.libs.crypto.base import MD5Hasher, SHA256Hasher, SHABaseHasher

def sumBase(content: str, h: SHABaseHasher) -> str:
    h.update_str(content)
    rv: str = h.get_hash()
    return rv

def Sum256(content: str) -> str:
    return sumBase(content=content, h=SHA256Hasher())

def SumMD5(content: str) -> str:
    return sumBase(content=content, h=MD5Hasher())

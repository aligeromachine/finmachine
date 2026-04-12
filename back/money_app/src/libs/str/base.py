import random
import re
import string
import uuid

def last_digits(s: str) -> int:
    ret = re.findall(r'\d+', s)
    return ret[-1] if ret else 0

def escape_chars(s: str) -> str:
    # '_', '-', '.' or space with an '_'.
    return re.sub(r"[^\w\-_. ]", "_", s)

def escape_sql(s: str) -> str:
    s = re.sub(r"'", r"''", s)
    s = re.sub(r'\\', r'\\\\', s)
    return s

def trim_ctx(content: str) -> str:
    raw = [it.strip() for it in content.splitlines()]
    return '\n'.join(raw)

def getDigit(s: str) -> str:
    digits = ''.join(filter(str.isdigit, s))
    return digits

def isDigit(s: str) -> bool:
    if not s:
        return False

    return s == getDigit(s=s)

def random_string(size: int = 15) -> str:
    characters = string.ascii_letters
    random_string = ''.join(random.choice(characters) for _ in range(size))
    return random_string.lower()

def CreateGuid() -> str:
    return str(uuid.uuid4())

def generate_digits_letters(length: int = 5) -> str:
    characters = string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def get_len_from_salt(fname: str) -> int:
    fname = fname[::-1]
    match = re.search(r"\$([^$]+)?\$", fname)
    if match:
        if match.group(0) == '$$':
            return 0
    return len(match.group(1)) if match else 0

def smart_fix_single_quotes(json_str: str) -> str:
    pattern = r"'([^']*)'"
    return re.sub(pattern, r'"\1"', json_str)

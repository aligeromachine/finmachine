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
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(size)).lower()

def CreateGuid() -> str:
    return str(uuid.uuid4())

def generate_digits_letters(length: int = 5) -> str:
    # Define the pool of characters to choose from (only letters)
    characters = string.digits
    # Generate a random string of the specified length
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

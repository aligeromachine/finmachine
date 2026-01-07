from typing import Callable
import re
from libs.types.exp import TBaseModel

X: Callable = lambda a: '' if not isinstance(a, list) else str(a[0]) if len(a) > 0 else ''
XX: Callable = lambda a: a[0] if len(a) > 0 else ''
Y: Callable = lambda a, b: a[b] if (a and b in a) else ''
YX: Callable = lambda a, b: a[b] if (b in a) else ''
xSQL: Callable = lambda ls: ','.join([f"'{it}'" for it in ls])
XELM: Callable = lambda ls: ls[0] if len(ls) > 0 else None
XKEY: Callable = lambda key, d: d[key] if key in d else ''
DEFAULT: Callable = lambda a: a if a else ''
remove_spec = lambda x: re.sub(r"['\" ]", "", x)
cal_bell: Callable = lambda ed, md: True if not ed and md else ed < md if md else False
dump_model: Callable[[TBaseModel | dict | None], dict | None] = lambda data: (data if isinstance(data, dict) else data.model_dump()) if data else None
slov_sorted: Callable[[dict[str, str]], dict[str, str]] = lambda slov: dict(sorted(slov.items(), key=lambda item: item[0].lower()))
check_def: Callable[[str], str] = lambda x: x if x else "-"

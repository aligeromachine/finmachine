import logging
from pathlib import Path
from libs.const import CONST

logger = logging.getLogger(__name__)

def conver_to_path(pth: str) -> Path | None:
    if not pth:
        return None
    return Path(pth)

def safe_remove(pth: str, remove_root: bool = False) -> None:
    p = conver_to_path(pth=pth)
    if not p or not p.exists():
        return

    if p.is_file() or p.is_symlink():
        p.unlink()
        return

    if p.is_dir():
        for it in p.iterdir():
            safe_remove(pth=str(it.resolve()), remove_root=remove_root)

    if remove_root:
        if p.exists() and not len([it for it in p.iterdir()]):
            if p.is_dir():
                p.rmdir()

def empty_remove(pth: str) -> None:
    p = conver_to_path(pth=pth)
    if not p or not p.exists():
        return

    if not p.is_dir():
        return

    if not len([it for it in p.iterdir()]):
        p.rmdir()
    else:
        for it in p.iterdir():
            if it.is_dir():
                empty_remove(pth=str(it.resolve()))

def count_files(pth: str) -> int:
    initial_count: int = 0
    p = conver_to_path(pth=pth)
    if not p or not p.exists():
        return initial_count

    for p in p.iterdir():
        if p.is_file():
            initial_count += 1
        if p.is_dir():
            initial_count += count_files(str(p.resolve()))

    return initial_count

def write_context(pth: str, content: str | bytes) -> None:
    p = conver_to_path(pth=pth)
    if not p:
        return

    if isinstance(content, str):
        p.write_text(content, encoding='utf-8')

    if isinstance(content, bytes):
        p.write_bytes(content)

def append_context(pth: str, content: str) -> None:
    p = conver_to_path(pth=pth)
    if not p:
        return

    existing_text = p.read_text(encoding='utf-8')
    new_text = existing_text + content
    p.write_text(new_text, encoding='utf-8')

def read_text_data(pth: str) -> str:
    content: str = CONST.empty

    p = conver_to_path(pth=pth)
    if not p or not p.exists():
        return content

    try:
        content = p.read_text(encoding='utf-8').strip()
    except Exception as ex:
        logger.error(ex)

    return content

def read_byte_data(pth: str) -> bytes:
    content: bytes = CONST.emptyb

    p = conver_to_path(pth=pth)
    if not p or not p.exists():
        return content

    try:
        content = p.read_bytes()
    except Exception as ex:
        logger.error(ex)

    return content

def file_exist(pth: str) -> bool:
    p = conver_to_path(pth=pth)
    if not p:
        return False
    return p.exists()

def name_file(pth: str) -> str:
    p = conver_to_path(pth=pth)
    if not p:
        return ''
    return p.name

def stem_name_file(pth: str) -> str:
    p = conver_to_path(pth=pth)
    if not p:
        return ''
    return p.stem

def suffix_name_file(pth: str) -> str:
    p = conver_to_path(pth=pth)
    if not p:
        return ''
    return p.suffix

def name_dir(pth: str) -> str:
    p = conver_to_path(pth=pth)
    if not p:
        return ''
    return str(p.parent)

def file_folder_to_list_name(pth: str) -> list[Path]:
    ls: list[Path] = []

    p = conver_to_path(pth=pth)
    if not p or not p.exists():
        return ls

    ls = []
    for it in p.iterdir():

        if it.is_file():
            ls.append(it)

        if it.is_dir():
            ls.extend(file_folder_to_list_name(str(it.resolve())))

    return ls

def gather_chink(pth: str, hash_sum: str) -> str:
    read_files = ''

    p = conver_to_path(pth=pth)
    if not p or not p.exists():
        return read_files

    ls = [it.resolve() for it in p.iterdir() if it.name.startswith(hash_sum)]
    ls = sorted(ls, key=lambda x: int(x.name[len(hash_sum) + 1:]))

    for it in ls:

        with open(it.resolve(), encoding='utf-8') as f:
            read_files += f.read()

    for it in p.iterdir():
        if it.name.startswith(hash_sum):
            it.unlink()

    return read_files

def file_size(pth: str) -> int:
    p = conver_to_path(pth=pth)
    if not p:
        return 0
    if not p.exists():
        return 0
    if p.is_file():
        return p.stat().st_size
    return 0

def make_dir(pth: str) -> str | None:
    p = conver_to_path(pth=pth)
    if not p:
        return None
    if p.exists():
        return str(p.resolve())
    p.mkdir(mode=0o777, exist_ok=True)
    return str(p.resolve())

def abs_path(*parts: str) -> str:
    p = Path(*parts)
    return str(p.resolve())

import logging
from pathlib import Path
from money.libs.const import CONST

logger = logging.getLogger(__name__)

def safe_remove(pth: str, remove_root: bool = False) -> None:
    p: Path = Path(pth)

    if not p.exists():
        return

    if p.is_file() or p.is_symlink():
        p.unlink()
        return

    if p.is_dir():
        for it in p.iterdir():
            safe_remove(pth=str(it.resolve()), remove_root=True)

    if remove_root:
        if p.exists() and not len([it for it in p.iterdir()]):
            if p.is_dir():
                p.rmdir()

def empty_remove(pth: str) -> None:
    p: Path = Path(pth)

    if not p.exists():
        return

    if not p.is_dir():
        return

    if not len([it for it in p.iterdir()]):
        p.rmdir()
    else:
        for it in p.iterdir():
            if it.is_dir():
                empty_remove(pth=str(it.resolve()))

def count_files(nf: str) -> int:

    initial_count: int = 0
    for p in Path(nf).iterdir():
        if p.is_file():
            initial_count += 1
        if p.is_dir():
            initial_count += count_files(str(p.resolve()))

    return initial_count

def write_context(pth: str, content: str | bytes, mode: str = 'w') -> None:
    p: Path = Path(pth)
    with p.open(mode=mode, encoding='utf-8') as f:
        if isinstance(content, str):
            f.write(content)

def read_text_data(pth: str) -> str:
    content: str = CONST.empty

    p: Path = Path(pth)
    if not p.exists():
        return content

    with p.open(encoding='utf-8') as f:
        try:
            content = f.read().strip()
        except Exception as ex:
            logger.error(ex)

    return content

def read_byte_data(pth: str) -> bytes:
    content: bytes = CONST.emptyb

    p: Path = Path(pth)
    if not p.exists():
        return content

    with p.open(mode='rb', encoding='utf-8') as f:
        try:
            content = f.read()
        except Exception as ex:
            logger.error(ex)

    return content

def file_exist(pth: str) -> bool:
    p: Path = Path(pth)
    return p.exists()

def name_file(pth: str) -> str:
    return Path(pth).name

def stem_name_file(pth: str) -> str:
    return Path(pth).stem

def suffix_name_file(pth: str) -> str:
    return Path(pth).suffix

def name_dir(pth: str) -> str:
    return str(Path(pth).parent)

def file_folder_to_list_name(pth: str) -> list[Path]:
    ls: list[Path] = []

    p: Path = Path(pth)
    if not p.exists():
        return ls

    ls = []
    for it in p.iterdir():

        if it.is_file():
            ls.append(it)

        if it.is_dir():
            ls.extend(file_folder_to_list_name(str(it.resolve())))

    return ls

def file_size(pth: str) -> int:
    p = Path(pth)
    if p.is_file():
        return p.stat().st_size
    return 0

def make_dir(pth: str) -> str:
    p = Path(pth)
    p.mkdir(mode=0o777, exist_ok=True)
    return str(p.resolve())

def abs_path(*parts: str) -> str:
    p = Path(*parts)
    return str(p.resolve())

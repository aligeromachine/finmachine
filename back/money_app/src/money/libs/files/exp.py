import csv
from io import StringIO
from typing import Iterator
from .base import abs_path, file_exist, make_dir, safe_remove

def RemoveFile(path: str) -> None:
    safe_remove(pth=path)

def RemoveFolders(path: str, remove_root: bool = False) -> None:
    safe_remove(pth=path, remove_root=remove_root)

def ClearFile(pth: str) -> None:
    if not file_exist(pth):
        return
    with open(pth, "w") as _:
        pass

def create_directory(a: str, b: str) -> str:
    return make_dir(pth=abs_path(a, b))

def write_csv_list(nfile: str, ls: list) -> None:
    if not ls:
        return

    with open(nfile, 'w') as fcsv:

        csv_writer = csv.writer(fcsv)
        for it in ls:
            csv_writer.writerow(it)

def read_file_csv_list(pth: str) -> list:
    ls: list = []

    if not file_exist(pth):
        return ls

    with open(pth) as csv_file:
        reader = csv.reader(csv_file, dialect=csv.excel)
        headings = next(reader)
        ls = [row for row in reader if row]

    return ls

def read_payload_csv_list(payload: str) -> list:
    ls: list = []

    reader = csv.reader(StringIO(payload), dialect=csv.excel)
    headings = next(reader)
    ls = [row for row in reader if row]

    return ls

def ReadFileToList(pth: str) -> list:
    ls: list = []
    with open(pth) as f:

        while True:

            line = None

            try:
                line = f.readline()
            except: # noqa
                pass

            if not line:
                break

            ls.append(line.strip())

    return ls

def ReadFileSeekls(file_path: str, delta: int, start_pos: int) -> tuple:

    rng = []
    theend = False
    last_pos = 0

    with open(file_path) as f:

        f.seek(start_pos)

        for _ in range(delta):

            line = None

            try:
                line = f.readline().strip()
            except: # noqa
                pass

            if not line:
                theend = True
                break

            rng.append(line)

        last_pos = f.tell()

    return rng, theend, last_pos

def ReadFileSeekRaw(file_path: str, start_pos: int) -> tuple:

    rng = ''
    theend = False
    last_pos = 0

    with open(file_path) as f:
        f.seek(start_pos)

        line = None

        try:
            line = f.read().strip()
        except: # noqa
            pass

        if line:
            rng = line

        last_pos = f.tell()

    return rng, theend, last_pos

def split_list_yield(ls: list, chunk_size: int) -> Iterator[list]:
    for it in range(0, len(ls), chunk_size):
        yield ls[it:it + chunk_size]

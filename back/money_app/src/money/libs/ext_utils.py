from money.libs.ext_c import CONST
from pathlib import Path
from typing import Iterator, Callable
from datetime import datetime, timedelta
import csv
import os
import random
import re
import string
import uuid
import hashlib
import shutil

X: Callable = lambda a: CONST.empty if not isinstance(a, list) else str(a[0]) if len(a) > 0 else CONST.empty
XX: Callable = lambda a: a[0] if len(a) > 0 else CONST.empty
Y: Callable = lambda a, b: a[b] if (a and b in a) else CONST.empty
YX: Callable = lambda a, b: a[b] if (b in a) else CONST.empty
DaysBeforeNow: Callable = lambda a: (datetime.now() - timedelta(days=a)).timestamp()
DaysDeltaNow: Callable = lambda a: (datetime.now() - timedelta(days=a))
timeX: Callable = lambda: (datetime.now() - timedelta(hours=4)).strftime("%H-%M-%S")
timeF: Callable = lambda: (datetime.now() + timedelta(hours=3)).strftime('%d-%m-%Y_%H-%M-%S')
timeSQL: Callable = lambda a: (a).strftime('%Y-%m-%d %H:%M:%S')
timeDRF: Callable = lambda dt: (dt).strftime('%Y-%m-%d %H:%M:%S') if dt else CONST.empty
timeDRFF: Callable = lambda dt: (dt).strftime('%d-%m-%Y %H:%M:%S') if dt else CONST.empty
dateDRF: Callable = lambda dt: (dt).strftime('%d-%m-%Y') if dt else CONST.empty
timeDRFstr: Callable = lambda dt: ' '.join((dt.split('Z'))[0].split('T')) if dt else CONST.empty
xSQL: Callable = lambda ls: ','.join([f"'{it}'" for it in ls])
XELM: Callable = lambda ls: ls[0] if len(ls) > 0 else None
XKEY: Callable = lambda key, d: d[key] if key in d else CONST.empty
DEFAULT: Callable = lambda a: a if a else CONST.empty

def CreateGuid() -> str:
    return str(uuid.uuid4())

def DeltaDateTime(h: int = 3) -> datetime:
    return datetime.now() + timedelta(hours=h)

def CliverDateTime(h: int = 3) -> datetime:
    data = datetime.now() + timedelta(hours=h)
    delta = datetime(
        year=data.year,
        month=data.month,
        day=data.day,
        hour=data.hour,
        minute=data.minute,
        second=data.second
    )
    return delta

def LogTime(h: int = 0) -> str:
    return DeltaDateTime(h).strftime(CONST.FormatT)

def RemoveFile(path: str) -> None:
    try:
        os.remove(path)
    except: # noqa
        pass

def RemoveFolders(path: str, remove_root: bool = True) -> None:
    if not os.path.isdir(path):
        return

    # remove empty subfolders
    files = os.listdir(path)
    for f in files:
        full_path = os.path.join(path, f)
        if os.path.isdir(full_path):
            RemoveFolders(full_path)
        if os.path.isfile(full_path):
            RemoveFile(full_path)

    if os.path.exists(path) and len(os.listdir(path)) == 0 and remove_root:
        if os.path.isdir(path):
            os.rmdir(path)

def ClearFolders(pth: str) -> None:

    if os.path.exists(pth):

        if os.path.isdir(pth):

            if not len(os.listdir(pth)):
                os.rmdir(pth)
            else:
                for f in os.listdir(pth):
                    full_path = os.path.join(pth, f)

                    if os.path.isdir(full_path):
                        ClearFolders(full_path)

def CountFilesFolder(nf: str) -> int:

    initial_count: int = 0
    for path in Path(nf).iterdir():
        if path.is_file():
            initial_count += 1
        if path.is_dir():
            initial_count += CountFilesFolder(str(path.resolve()))

    return initial_count

def WriteToFile(pth: str, content: str | bytes, flag: str) -> None:
    with open(pth, flag) as f:
        f.write(content)

def ReadFileContent(pth: str) -> str:
    with open(pth, encoding=CONST.UTF8, errors='ignore') as f:
        return f.read()

def CopyFile(src: str, dst: str) -> bool:
    if os.path.isfile(src):
        shutil.copyfile(src=src, dst=dst)

    return os.path.isfile(dst)

def RandomName(size: int = 15) -> str:
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(size)).lower()

def CreateDirectory(a: str, b: str) -> str:
    dir_report = AbsPath(a, b)
    if not os.path.exists(dir_report):
        try:
            os.mkdir(dir_report)
        except: # noqa
            pass

    return dir_report

def AbsPath(*argv: str) -> str:
    return str(os.path.abspath(os.path.join(*argv)))

def WriteLsToCSV(nfile: str, ls: list) -> None:

    if not ls:
        return

    with open(nfile, 'w') as fcsv:
        csv_writer = csv.writer(fcsv)

        for it in ls:
            csv_writer.writerow(it)

def ReadStdCsv(pth: str) -> list:
    ls: list = []

    if os.path.isfile(pth):
        with open(pth) as csv_file:
            ls = [it for it in csv.reader(csv_file, dialect=csv.excel)]

    return ls

def reder_csv(pth: str):
    import csv
    ls = []
    with open(pth, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Skip/save header row
        header = next(reader) # noqa  
        for row in reader:
            # Process each row (list of strings)
            ls.append(row)

    return ls

def ReadUniqCsv(pth: str) -> list:
    ls: list = []

    def addls(fl: str) -> None:
        for it in ReadFileToList(fl):
            actions = re.split(r'[\t,]', it.strip())
            if len(actions) > 0:
                ls.append(actions)

    if os.path.isfile(pth):
        addls(fl=pth)

    if os.path.isdir(pth):
        for it in os.listdir(pth):
            addls(fl=AbsPath(pth, it))

    return ls

def ReadFileToList(pth: str) -> list:
    ls: list = []

    with open(pth) as f:

        while True:

            line = CONST.error_data

            try:
                line = f.readline()
            except: # noqa
                pass

            if not line:
                break

            if line is CONST.error_data:
                continue

            if line is CONST.empty:
                continue

            ls.append(line.strip())

    return ls

def RemoveDuplicateLs(items: list) -> list:
    return list(set(items))

def Sum256(content: str | bytes) -> str:
    data = CONST.emptyb
    if isinstance(content, str):
        data = content.encode()
    if isinstance(content, bytes):
        data = content

    return hashlib.sha256(data).hexdigest()

def SumMD5(content: str | bytes) -> str:
    data = CONST.emptyb
    if isinstance(content, str):
        data = content.encode()
    if isinstance(content, bytes):
        data = content

    return hashlib.md5(data).hexdigest()

def ExtractDigits(s: str) -> str:
    return ''.join([i for i in str(s) if i.isdigit()])

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

def RangesTols(ls_raw: list) -> list:
    ls: list = []

    if not ls_raw:
        return ls

    ls_int = [it for it in ls_raw if isinstance(it, int)]
    ls_ls = [it for it in ls_raw if isinstance(it, list)]
    ls.extend(ls_int)
    for it in ls_ls:
        begin = it[0]
        end = it[1]
        ls.extend(list(range(begin, end + 1)))

    ls = sorted(list(set(ls)))
    return ls

def ReadFileSeekls(file_path: str, delta: int, start_pos: int) -> tuple:

    rng = []
    theend = False
    last_pos = 0

    with open(file_path) as f:

        f.seek(start_pos)

        for _ in range(delta):

            line = CONST.empty

            try:
                line = f.readline()
            except: # noqa
                pass

            if not line:
                theend = True
                break

            if line == CONST.empty:
                continue

            rng.append(line.strip())

        last_pos = f.tell()

    return rng, theend, last_pos


def ReadFileSeekRaw(file_path: str, start_pos: int) -> tuple:

    rng = CONST.empty
    theend = False
    last_pos = 0

    with open(file_path) as f:
        f.seek(start_pos)

        line = CONST.empty

        try:
            line = f.read()
        except: # noqa
            pass

        if line and line != CONST.empty:
            rng = line.strip()

        last_pos = f.tell()

    return rng, theend, last_pos

def NamelsFilesFolder(nf: str) -> list[Path]:
    ls = []
    for path in Path(nf).iterdir():
        if path.is_file():
            ls.append(path)
        if path.is_dir():
            ls.extend(NamelsFilesFolder(str(path.resolve())))

    return ls

def file_xize(file_path: str) -> int:
    if os.path.isfile(file_path):
        return os.path.getsize(file_path)
    return 0

def ClearFile(pth: str) -> None:
    with open(pth, "w") as f: # noqa
        pass

def split_list_yield(ls: list, chunk_size: int) -> Iterator[list]:
    for it in range(0, len(ls), chunk_size):
        yield ls[it:it + chunk_size]

def getDigit(s: str) -> str:
    digits = ''.join(filter(str.isdigit, s))
    return digits

def isDigit(s: str) -> bool:
    if not s:
        return False

    return s == getDigit(s=s)

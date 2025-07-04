import os
import gzip
import base64
import tarfile
from money.libs.ext_c import CONST
from money.libs.ext_utils import RemoveFile
import zlib

def compress_string(input_string: str) -> str:
    input_bytes = input_string.encode('utf-8')
    compressed_bytes = zlib.compress(input_bytes)
    compressed_string = base64.b64encode(compressed_bytes).decode('utf-8')

    return compressed_string

def decompress_bytes(compressed_string: bytes) -> str:
    compressed_bytes = base64.b64decode(compressed_string)
    decompressed_bytes = zlib.decompress(compressed_bytes)
    decompressed_string = decompressed_bytes.decode('utf-8')

    return decompressed_string

def decompress_string(compressed_string: str) -> str:

    return decompress_bytes(compressed_string=compressed_string.encode('utf-8'))

def ExtractTarFile(name_file: str, name_dir: str, delete: bool = True) -> None:

    try:
        with tarfile.open(name_file) as tf:
            tf.extractall(name_dir)
    except: # noqa
        pass

    if delete:
        RemoveFile(name_file)

def DirToTarFile(name_file: str, name_dir: str) -> bool:
    with tarfile.open(name_file, 'w:gz') as archive:
        for it in [name for name in os.listdir(name_dir)]:
            fn = f'{name_dir}/{it}'
            archive.add(fn)

    return os.path.isfile(name_file)

def ContentByte_GzipStr(content_bytes: bytes) -> str:
    data: str = CONST.empty

    try:
        zip_raw = gzip.compress(content_bytes)
        zip_b64 = base64.b64encode(zip_raw)
        data = zip_b64.decode()
    except: # noqa
        pass

    return data

def GzipStr_ContentByte(data: str) -> bytes:
    content_bytes: bytes = CONST.emptyb

    try:
        zip_b64 = data.encode()
        zip_raw = base64.b64decode(zip_b64)
        content_bytes = gzip.decompress(zip_raw)
    except: # noqa
        pass

    return content_bytes

def ContentCompress(content: str) -> str:
    content_bytes: bytes = content.encode()
    rv: str = ContentByte_GzipStr(content_bytes)
    return rv

def ContentDeCompress(data: str) -> str:
    content_bytes = GzipStr_ContentByte(data)
    return content_bytes.decode()

def File_GzipStr(pth: str) -> str:
    content: str = CONST.empty

    with open(pth, 'rb') as f:
        content = ContentByte_GzipStr(f.read())

    return content

def GzipStr_File(pth: str, content: str) -> None:
    content_bytes = GzipStr_ContentByte(content)

    if content_bytes == CONST.emptyb:
        return

    with open(pth, 'wb') as f:
        f.write(content_bytes)

def B64Str_ContentByte(content: str) -> bytes:

    if not content:
        return bytes(CONST.emptyb)

    content_bytes = base64.b64decode(content.encode())

    return content_bytes

def ContentByte_B64Str(content_bytes: bytes) -> str:

    b64str = base64.b64encode(content_bytes).decode()

    return b64str

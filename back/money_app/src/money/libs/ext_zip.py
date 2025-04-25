import os
import gzip
import base64
import tarfile
from money.libs.ext_c import CONST
from money.libs.ext_utils import RemoveFile
import zlib
import logging
logger = logging.getLogger(__name__)

def compress_string(input_string: str):
    input_bytes = input_string.encode('utf-8')
    compressed_bytes = zlib.compress(input_bytes)
    compressed_string = base64.b64encode(compressed_bytes).decode('utf-8')

    return compressed_string

def decompress_bytes(compressed_string: bytes):
    compressed_bytes = base64.b64decode(compressed_string)
    decompressed_bytes = zlib.decompress(compressed_bytes)
    decompressed_string = decompressed_bytes.decode('utf-8')

    return decompressed_string

def decompress_string(compressed_string: str):
    return decompress_bytes(compressed_string=compressed_string.encode('utf-8'))

def ExtractTarFile(name_file: str, name_dir: str, delete: bool = True):

    try:
        with tarfile.open(name_file) as tf:
            tf.extractall(name_dir)
    except Exception as ex:
        logger.error(ex)

    if delete:
        RemoveFile(name_file)

def DirToTarFile(name_file: str, name_dir: str):
    with tarfile.open(name_file, 'w:gz') as archive:
        for it in [name for name in os.listdir(name_dir)]:
            fn = '{}/{}'.format(name_dir, it)
            archive.add(fn)

    return os.path.isfile(name_file)

def ContentByte_GzipStr(content_bytes: bytes):
    data = CONST.empty

    try:
        zip_raw = gzip.compress(content_bytes)
        zip_b64 = base64.b64encode(zip_raw)
        data = zip_b64.decode()
    except Exception as ex:
        logger.error(ex)

    return data

def GzipStr_ContentByte(data: str):
    content_bytes = CONST.emptyb

    try:
        zip_b64 = data.encode()
        zip_raw = base64.b64decode(zip_b64)
        content_bytes = gzip.decompress(zip_raw)
    except Exception as ex:
        logger.error(ex)

    return content_bytes

def ContentCompress(content: str):
    content_bytes = content.encode()
    return ContentByte_GzipStr(content_bytes)

def ContentDeCompress(data: str):
    content_bytes = GzipStr_ContentByte(data)
    return content_bytes.decode()

def File_GzipStr(pth: str):
    content = CONST.empty

    with open(pth, 'rb') as f:
        content = ContentByte_GzipStr(f.read())

    return content

def GzipStr_File(pth: str, content: str):
    content_bytes = GzipStr_ContentByte(content)

    if content_bytes == CONST.emptyb:
        return

    with open(pth, 'wb') as f:
        f.write(content_bytes)

def B64Str_ContentByte(content: str):

    if content == CONST.empty:
        return CONST.emptyb

    if not content:
        return CONST.emptyb

    content_bytes = base64.b64decode(content.encode())

    return content_bytes

def ContentByte_B64Str(content_bytes: bytes):

    b64str = base64.b64encode(content_bytes).decode()

    return b64str

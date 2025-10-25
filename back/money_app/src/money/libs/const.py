class CONST:
    POST: str = 'POST'
    GET: str = 'GET'
    PUT: str = 'PUT'
    empty: str = ''
    emptyb: bytes = b''
    emptyls: list = [empty, None]
    FormatT: str = '%d-%m-%Y %H:%M:%S'
    FormatDDP: str = '%Y-%m-%d %H:%M:%S'
    FormatFull: str = '%Y-%m-%dT%H:%M:%S.%fZ'
    FormatAccess: str = '%m/%d/%y %H:%M:%S'
    DtRaw: str = '%Y-%m-%d %H:%M:%S.%fz'
    FormatF: str = '%d-%m-%Y_%H-%M-%S'
    FTime: str = '%H:%M:%S'
    FDate: str = '%Y-%m-%d'
    csrftoken: str = 'csrfmiddlewaretoken'
    timeout: int = 10
    localhost: str = '127.0.0.1'
    UTF8: str = 'utf-8'
    ASCII: str = 'ascii'
    session_null: bytes = b'\x00\x00\x00\x00'
    zero: str = '0'
    DAY_BEGIN: str = '00:00:00'
    DAY_END: str = '23:59:59'
    CHUNK_SIZE: int = 100
    HASH_ID: str = 'hash_id'
    TASK_ID: str = 'task_id'
    data: str = 'data'
    raw: str = 'raw'

TIMEOUT: tuple = (2, 5)
HEADERS: dict = {
    "Content-Type": "application/json", 
    "Cache-Control": "no-cache",
    "Accept": "*/*",
}
MAX_TRY_COUNT: int = 5
PARTS_SIZE: int = 1_024 * 250
PROXY_CRUSH: dict = {
    "http": "socks5://127.0.0.1:10000",
    "https": "socks5://127.0.0.1:10000",
}
HEADERS_MOZILA: dict = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0", 
    "Accept": "application/json, text/plain, */*", 
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
}

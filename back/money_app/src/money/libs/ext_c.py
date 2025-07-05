class CONST:
    POST = 'POST'
    GET = 'GET'
    PUT = 'PUT'
    empty = str('')
    emptyb = b''
    emptyls = [empty, None]
    FormatT = '%d-%m-%Y %H:%M:%S'
    FormatDDP = '%Y-%m-%d %H:%M:%S'
    FormatAccess = '%m/%d/%y %H:%M:%S'
    FormatFull = '%Y-%m-%dT%H:%M:%S.%fZ'
    FTime = '%H:%M:%S'
    FDate = '%Y-%m-%d'
    csrftoken = 'csrfmiddlewaretoken'
    data = 'data'
    type_b = 'b'
    type_s = 's'
    type_json = 'json'
    type_dict = 'dict'
    sep_task = ','
    timeout = 10
    addr = 'addr'
    localhost = '127.0.0.1'
    error_data = 'error_data'
    empty_data = 'empty_data'
    UTF8 = 'utf-8'
    ASCII = 'ascii'
    admin = 'admin'
    session_null = b'\x00\x00\x00\x00'
    empty_rec = '__'
    automat = 'automat'
    zero = '0'
    DAY_BEGIN = '00:00:00'
    DAY_END = '23:59:59'


# ******** GATE  ******** #
###########################
class GateResponse:
    bot_state = 'bot_state'
    rep_data = 'rep_data'


class Extensions:
    tar = '.tar'
    targz = '.targz'
    xml = '.xml'
    csv = '.csv'
    txt = '.txt'
    xls = '.xls'
    json = '.json'


class PathNames:
    info = "info"
    results = "results"
    export = "export"
    task_files = "task_files"
    statist = "statist"
    token = "token"
    tunel = "tunel"
    crusher = "crusher"
    wordlist = "wordlist"
    exchange = "exchange"
    auto = "auto"
    raw = "raw"

    const_path = '/home/data/media/task_files/'


# Resposne Bot
class RequestEx:
    data = 'data'
    chink = 'chink'


class HtmlPage:
    dashboard = 'dashboard'
    userprofile = 'userprofile'
    chart = 'chart'
    tercus = 'tercus'
    tasks = 'tasks'
    export = 'export'
    hashtype = 'hashtype'
    logger = 'logger'
    access = 'access'
    digaro = 'digaro'
    files = 'files'
    utilits = 'utilits'
    exchange = 'exchange'

    front = 'front'

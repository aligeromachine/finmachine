import os
from money.ext_func.ext_utils import (
    AbsPath, 
    CreateDirectory)
from service.settings import MEDIA_ROOT
from datetime import datetime
from money.ext_func.ext_c import (
    CONST, 
    PathNames)

def create_task_dir(name: str, dt: datetime):
    folder = CreateDirectory(a=MEDIA_ROOT, b=name)
    folder = CreateDirectory(a=folder, b=dt.strftime('%Y'))
    folder = CreateDirectory(a=folder, b=dt.strftime('%m'))
    folder = CreateDirectory(a=folder, b=dt.strftime('%d'))

    return folder

def put_file_base(nf: str, dt: datetime, prefix: str):
    if not dt:
        return CONST.empty
    
    if nf in CONST.emptyls:
        return CONST.empty
    
    folder = create_task_dir(name=prefix, dt=dt)

    file_path = AbsPath(folder, nf)

    return file_path

def get_file_base(nf: str, dt: datetime, prefix: str):

    if not dt:
        return CONST.empty
    
    if nf in CONST.emptyls:
        return CONST.empty

    return AbsPath(MEDIA_ROOT, prefix, dt.strftime('%Y'), dt.strftime('%m'), dt.strftime('%d'), nf)

def get_statist_report_grah():

    folder = AbsPath(MEDIA_ROOT, PathNames.info)
    if not os.path.exists(folder):
        os.mkdir(folder)

    return AbsPath(folder, "stat_grah.json")

def get_statist_report_round():

    folder = AbsPath(MEDIA_ROOT, PathNames.info)
    if not os.path.exists(folder):
        os.mkdir(folder)

    return AbsPath(folder, "stat_round.csv")

def get_base_crusher(name: str):

    folder = AbsPath(MEDIA_ROOT, PathNames.crusher)
    if not os.path.exists(folder):
        os.mkdir(folder)

    return AbsPath(folder, name)

def get_raw_path():

    folder = AbsPath(MEDIA_ROOT, PathNames.raw)
    if not os.path.exists(folder):
        os.mkdir(folder)

    return AbsPath(folder)

def get_crusher_code():
    return get_base_crusher("code.json")

def get_crusher_attack():
    return get_base_crusher("attack.json")

def get_token_path(type_token: str, ext: str = ".txt"):

    folder = AbsPath(MEDIA_ROOT, PathNames.token)
    if not os.path.exists(folder):
        os.mkdir(folder)

    return AbsPath(folder, f"{type_token}{ext}")

def get_work_token():
    return get_token_path(type_token="work", ext="")

def get_access_token():
    return get_token_path("access")

def get_refresh_token():
    return get_token_path("refresh")

def get_session_token():
    return get_token_path("session")

def get_store_token():
    return get_token_path("session_cookie", ".plk")

def put_task_file(nf: str, dt: datetime):

    return put_file_base(nf=nf, dt=dt, prefix=PathNames.task_files)

def _get_file_href_base(nf: str, dt: datetime, prefix: str):

    return get_file_base(nf=nf, dt=dt, prefix=prefix).replace(MEDIA_ROOT, '')

def get_task_file(nf: str, dt: datetime):

    return get_file_base(nf=nf, dt=dt, prefix=PathNames.task_files)

def get_task_file_href(nf: str, dt: datetime):

    return _get_file_href_base(nf, dt, PathNames.task_files)

def put_export_file(nf: str, dt: datetime):

    return put_file_base(nf=nf, dt=dt, prefix=PathNames.export)

def get_export_file(nf: str, dt: datetime):

    return get_file_base(nf=nf, dt=dt, prefix=PathNames.export)

def get_export_file_href(nf: str, dt: datetime):

    return _get_file_href_base(nf, dt, PathNames.export)

def put_statist_file(nf: str, dt: datetime):

    return put_file_base(nf=nf, dt=dt, prefix=PathNames.statist)

def get_statist_file(nf: str, dt: datetime):

    return get_file_base(nf=nf, dt=dt, prefix=PathNames.statist)

def get_statist_file_href(nf: str, dt: datetime):

    return _get_file_href_base(nf, dt, PathNames.statist)

def put_results_file(nf: str, dt: datetime):

    return put_file_base(nf=nf, dt=dt, prefix=PathNames.results)

def get_results_file(nf: str, dt: datetime):

    return get_file_base(nf=nf, dt=dt, prefix=PathNames.results)

def get_results_file_href(nf: str, dt: datetime):

    return _get_file_href_base(nf, dt, PathNames.results)

def put_tunel_file(nf: str, dt: datetime):

    return put_file_base(nf=nf, dt=dt, prefix=PathNames.tunel)

def get_tunel_file(nf: str, dt: datetime):

    return get_file_base(nf=nf, dt=dt, prefix=PathNames.tunel)

def get_tunel_file_href(nf: str, dt: datetime):

    return _get_file_href_base(nf, dt, PathNames.tunel)

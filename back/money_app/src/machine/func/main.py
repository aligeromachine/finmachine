from machine.const.code import MACHINE, TYPE_SCORE_CODE, MACHINE_SCORE_CODE


def base_speed_code(type_code: str, data: dict) -> str | None:
    key: str | None = None

    for k, v in data.items():

        ls = [str(it) for it in v]

        if type_code in ls:
            key = str(k)
            break

    return key

def speed_code_for_type_code(type_code: str) -> str | None:
    rv: str | None = base_speed_code(type_code=type_code, data=TYPE_SCORE_CODE)
    return rv

def machine_code_for_type_code(type_code: str) -> str | None:
    key: str | None = speed_code_for_type_code(type_code=type_code)
    rv: str | None = base_speed_code(type_code=key, data=MACHINE_SCORE_CODE)  # type: ignore
    return rv

def attaks_slov_for_type_code(type_code: str, data: dict) -> list:

    attak_speed: str | None = speed_code_for_type_code(type_code=type_code)
    attak_raw: list = [v for k, v in data.items() if k == attak_speed]

    names_attak: list = []
    for it in attak_raw:
        names_attak.extend(it)

    return names_attak

def get_codes_by_service(mac: str) -> list:

    scope_speed: list = MACHINE_SCORE_CODE[mac] if mac in MACHINE_SCORE_CODE else []

    if not scope_speed:
        return []

    ls: list = []
    ls_raw = [v for k, v in TYPE_SCORE_CODE.items() if k in scope_speed]
    for it in ls_raw:
        ls.extend(it)

    return ls

def get_codes_crusher() -> list:
    return get_codes_by_service(MACHINE.CRUSHER)

def get_codes_turcus() -> list:
    return get_codes_by_service(MACHINE.TERCUS)

def get_codes_polis() -> list:
    return get_codes_by_service(MACHINE.CRUSHER)

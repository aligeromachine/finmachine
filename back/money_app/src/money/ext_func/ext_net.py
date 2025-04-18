import ipaddress
import os
import re

from money.ext_func.ext_utils import AbsPath, ReadFileContent, ReadFileToList


def Get_client_ip(request: any):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def CheckValidIP(_ip):
    ret = False

    try:
        host_bytes = str(_ip).split('.')
        valid_raw = [int(b) for b in host_bytes]
        valid = [b for b in valid_raw if 0 <= b <= 255]
        if len(valid) == 4:
            ret = True
    except:
        pass

    return ret

def CheckValidPort(_port):
    ret = False

    try:
        b = int(_port)
        if 0 <= b <= 65365:
            ret = True
    except:
        pass

    return ret

# mask
def ParseSubMask(val: str):
    ls = [val]

    try:
        ls = [str(it.exploded) for it in ipaddress.ip_network(val).subnets()]
    except:
        pass

    return ls


def DevMask(txt: str, delta: int):

    if delta <= 1:
        return [txt]

    ls_ranges = []

    pat_raw = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}'
    pat = f'.*\s(?P<range>{pat_raw})\s'
    res = re.match(pat, f' {txt} '.split('--exclude')[0])

    result_range = ''

    if res:
        result_range = res.group('range')
        for itr in ParseSubMask(val=result_range):
            ls_ranges.append(itr)

    if len(ls_ranges) > 1:

        while True:

            if len(ls_ranges) >= delta:
                break

            ls = []

            for itr in ParseSubMask(val=ls_ranges[0]):
                ls.append(itr)

            ls_ranges.pop(0)

            for itr in ls:
                ls_ranges.append(itr)

    return [txt.replace(result_range, itr) for itr in ls_ranges] if len(ls_ranges) > 0 else [txt]


def DevMasscanConf(filename: str, delta: int, rpath: str):

    ret_ls = []

    content = ReadFileContent(pth=filename)
    
    pat_raw = 'range\s?=\s?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(/\d{1,2})?'   

    # range = 0.0.0.0/24
    
    pat = f'{pat_raw}'
    res = re.findall(pat, content)

    if len(res) == 0:
        return ret_ls

    ls = [it for it in ReadFileToList(filename) if not str(it).startswith('range') and len(it) != 0]

    if len(ls) == 0:
        return ret_ls

    import math

    len_ranges = math.ceil((len(res) / delta))

    nf = os.path.basename(filename)

    os.unlink(filename)    

    for index, it in enumerate(range(0, len(res), len_ranges)):
        rng = res[it:it + len_ranges]

        ls_ranges = []
        
        for em in ls:
            ls_ranges.append(em)

        ls_ranges.append('')
        
        for em in rng:
            ls_ranges.append(f'range = {em[0]}{em[1]}')

        file_out = AbsPath(rpath, f'{index + 1}_{nf}')

        ret_ls.append(file_out)

        with open(file_out, 'w') as f:
            for el in ls_ranges:
                f.writelines(f'{el}\n')
    
    return ret_ls

def MaskToRange(val: str):
    ls = []

    try:
        ls = [str(it.exploded) for it in ipaddress.IPv4Network(val)]
    except:
        pass
    
    return ls

    
def DevideMaskToMask(txt: str, delta: int):

    ls_ranges = []

    for it in ParseSubMask(val=txt):
        ls_ranges.append(it)

    if len(ls_ranges) > 1:

        while True:

            if len(ls_ranges) >= delta:
                break

            ls = []

            for itr in ParseSubMask(val=ls_ranges[0]):
                ls.append(itr)

            ls_ranges.pop(0)

            for itr in ls:
                ls_ranges.append(itr)

    return ls_ranges


def IP2Int(ip: str):
    addr = ip.split('.')
    res = 0
    if len(addr) == 4:
        o = list(map(int, addr))
        res = (16777216 * o[0]) + (65536 * o[1]) + (256 * o[2]) + o[3]
    return res


def Int2IP(ipnum: int):
    o1 = int(ipnum / 16777216) % 256
    o2 = int(ipnum / 65536) % 256
    o3 = int(ipnum / 256) % 256
    o4 = int(ipnum) % 256
    return f'{o1}.{o2}.{o3}.{o4}'


def ValidateLikeIpStr(Ip: str):
    ret = False

    regex = r"^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|\
    [1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|\
    [1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|\
    [1-9]?[0-9])(\.)?$"
    
    if not ret and re.search(regex, Ip):
        ret = True

    regex = r"^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|\
    [1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|\
    [1-9]?[0-9])(\.)?$"
    
    if not ret and re.search(regex, Ip):
        ret = True

    regex = r"^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.$"
    
    if not ret and re.search(regex, Ip):
        ret = True

    return ret


def ValidateIpStr(Ip: str):
    regex = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|\
    [1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    return True if re.search(regex, Ip) else False


def ValidateIpInt(Ip: str):
    regex = r"^\d{1,10}$"
    return True if re.search(regex, Ip) else False


def ValidateIpMaskSlash(Ip: str):
    regex = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|\
    [1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|\
    1[0-9][0-9]|[1-9]?[0-9])/(3[0-2]|2[0-9]|1[0-9]|[0-9])$"
    return True if re.search(regex, Ip) else False


def ValidateIpMaskline(Ip: str):
    
    regex = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|\
    [1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|\
    [1-9]?[0-9])-(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    return True if re.search(regex, Ip) else False


def MaskReplaseTo24(cmd: str):

    addr = r"((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|\
    [1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|\
    1[0-9][0-9]|[1-9]?[0-9])"
    regex = f"{addr}/(3[0-2]|2[0-9]|1[0-9]|[0-9])"

    if res := re.search(regex, cmd):
        result_range = res.group(4)
        range_int = int(result_range)
        if range_int < 24:
            rp = res.group(0).replace(f"/{result_range}", "/24")
            str_output = cmd.replace(res.group(0), rp)
            return str_output
    
    return cmd

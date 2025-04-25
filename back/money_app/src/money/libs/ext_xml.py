import os
import re
import xml.etree.ElementTree as ET
import logging
from money.libs.ext_c import CONST

logger = logging.getLogger(__name__)

class XML:
    result = "result"
    address = "address"
    address_addr = "addr"
    port = "port"
    port_portid = "portid"
    port_protocol = "protocol"


def ReadXmlMassCanFile(_f: str):
    ls = []

    if os.path.isfile(_f):
        with open(_f, 'r') as _file:

            while (True):
                # read next line
                line = CONST.empty
                try:
                    line = _file.readline()
                except Exception as ex:
                    logger.error(ex)

                if not line:
                    break

                pat = r'addr=\"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\".*portid=\"(\d{1,5})\"'
                result = re.search(pat, line)

                if result:

                    ls.append([result.group(1), result.group(2)])

    return ls

def ReadXmlNmapFile(_f: str):
    ls = []

    tree = ET.parse(_f)
    root = tree.getroot()

    _address = CONST.empty
    _port = CONST.empty

    _address_old = CONST.empty
    _port_old = CONST.empty

    for item in root.iter():

        if item.tag == XML.address:
            _address = item.get(XML.address_addr)

        if item.tag == XML.port:
            _port = item.get(XML.port_portid)

        if _port != _port_old or _address != _address_old:
            if CONST.empty not in [_address, _port]:
                ls.append([_address, _port])

                _port = CONST.empty
                _port_old = CONST.empty

            if _port != _port_old:
                _port_old = _port

            if _address != _address_old:
                _address_old = _address

    return ls

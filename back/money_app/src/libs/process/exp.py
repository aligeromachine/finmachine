import subprocess
from multiprocessing import Process
from typing import Callable
import logging
import re
import threading
import time
from libs.decore.calc_time import calculate_float_time
from libs.const import CONST

logger = logging.getLogger(__name__)

def SimpleProccess(func: Callable, arg: tuple) -> None:
    p = Process(target=func, args=arg)
    p.start()

def get_ip_address_subprocess(interface_name: str = 'eth1') -> str:
    try:

        output = subprocess.check_output(['ip', 'addr', 'show', interface_name])
        match = re.search(r'(\d+\.\d+\.\d+\.\d+)', output.decode('utf-8'))

        if match:
            return str(match.group(1)).strip()
        else:
            return "127.0.0.1"
    except subprocess.CalledProcessError:
        return "127.0.0.1"

def run_bash_out(cmd: str) -> str:

    result = ''

    try:
        p = subprocess.Popen(args=cmd, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

        if isinstance(output, bytes):
            result = output.decode()

        if isinstance(output, str):
            result = str(output)

    except Exception as ex:
        logger.error(str(ex))

    return result.strip()

def run_bash_out_trace(cmd: str, lp: bool = False, debug: bool = False) -> str:

    if lp:
        logger.info(cmd)

    result = ''

    if debug:
        logger.info(cmd)
        time.sleep(CONST.timeout)
    else:
        result = run_bash_out(cmd=cmd)

    return result

def run_bash(cmd: str) -> int:

    returned_value = 1

    try:
        returned_value = subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=True)
    except Exception as ex:
        logger.error(str(ex))

    return returned_value


@calculate_float_time  # type: ignore
def run_bash_trace(cmd: str, lp: bool = False, debug: bool = False) -> int:

    if lp:
        logger.info(cmd)

    returned_value = 1

    if debug:
        logger.info(cmd)
        time.sleep(CONST.timeout)
    else:
        returned_value = run_bash(cmd=cmd)

    return returned_value

@calculate_float_time  # type: ignore
def run_bash_terminate(cmd: str, finish_event: threading.Event, lp: bool = False, debug: bool = False) -> int:

    if lp:
        logger.info(cmd)

    result = 1

    if debug:
        logger.info(cmd)
        time.sleep(CONST.timeout)
    else:

        p = subprocess.Popen(cmd, stdin=None, stdout=None, stderr=None, shell=True)

        while True:

            if p.poll() is not None:
                break

            shutdown = finish_event.wait(1)

            if shutdown:
                logger.info("Поток получил сигнал остановки!")
                while p.poll() is None:
                    logger.info(f"task is finished. Terminating PID {p.pid}.")
                    p.terminate()
                    p.wait()
                    break

        result = p.returncode

    return result

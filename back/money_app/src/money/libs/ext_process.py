import subprocess
from typing import Callable
from multiprocessing import Process

def SimpleProccess(func: Callable, arg: tuple) -> None:
    p = Process(target=func, args=arg)
    p.start()

def RunSubProc(command: str) -> int:
    returned_value = 1

    try:
        returned_value = subprocess.call(command, stdin=None, stdout=None, stderr=None, shell=True)
    except: # noqa
        pass

    return returned_value

def RunCMD(command: str) -> str:

    result = ''

    try:
        p = subprocess.Popen(args=command, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

        if isinstance(output, bytes):
            result = output.decode()

        if isinstance(output, str):
            result = output

    except: # noqa
        pass

    return result

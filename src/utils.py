import os
import platform
from colorama import init
from termcolor import colored

init()


def createFolder(dir: str) -> None:
    """A async function to help create a folder by first checking if the folder already exists and
    if not it creates it and returns True. If it fails it returns false and araises an OSError"""
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
            print(colored(f"Directory {dir} created", "green"))

        else:
            raise OSError

    except OSError:
        print(colored(f"Error: directory {dir} already exists. ", "red"))

    except Exception as err:
        print(colored(f"Error: Creating directory {dir} due to {err!r}", "red"))


def check_os() -> str:
    """used to check the type of os being used"""
    return platform.system()


def pwd() -> str:
    """used to check the current working directory"""
    print(os.getcwd())
    return os.getcwd()

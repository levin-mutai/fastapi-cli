import os
from colorama import init, Fore
from termcolor import colored

init()


def createFolder(dir: str):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
            print(colored(f"Directory {dir} created", "green"))
        else:
            raise OSError
    except OSError:
        print(colored(f"Error: Creating directory {dir}. ", "red"))

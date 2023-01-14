import os
import asyncio
from colorama import init, Fore
from termcolor import colored

init()


async def createFolder(dir: str) -> bool:
    """A coroutine to help create a folder by first checking if the folder already exists and
    if not it creates it and returns True. If it fails it returns false and araises an OSError"""
    try:
        if not os.path.exists(dir):
            await os.makedirs(dir)
            print(colored(f"Directory {dir} created", "green"))
            return True
        else:
            raise OSError

    except OSError:
        print(colored(f"Error: Creating directory {dir}. ", "red"))
        return False

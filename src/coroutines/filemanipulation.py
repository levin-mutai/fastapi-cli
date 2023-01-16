import asyncio
import os

from ..context_mngs.file_manipulation import CreateFile
from utils import createFolder


async def create_multiple_files(files: list):
    for x in files:
        with CreateFile(x) as file:
            pass


async def create_folder_with_multiple_files(folder_name: str, files:list)
    await createFolder(folder_name)
    await os.chdir(folder_name)

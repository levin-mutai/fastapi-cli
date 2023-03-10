import asyncio
import os

# from ..context_mngs.file_manipulation import CreateFile, ChangeDir
from src.utils import createFolder
from src.context_mngs.file_manipulation import CreateFile, ChangeDir


async def create_multiple_files(files: list):
    for x in files:
        with open(x, "w") as file:
            file.close()


async def create_folder_with_multiple_files(folder_name: str, files: list):
    createFolder(folder_name)
    with ChangeDir(folder_name) as dir:
        await create_multiple_files(files)


create_folder_with_multiple_files("test", ["file1.py", "file2.py"])

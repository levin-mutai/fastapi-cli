import asyncio
import shutil
from src.utils import check_os, pwd
from src.coroutines.filemanipulation import (
    create_folder_with_multiple_files,
    create_multiple_files,
)

base_path = pwd()

platform_os = check_os()
print(platform_os)

loop = asyncio.new_event_loop()


def run():
    loop.run_until_complete(
        create_folder_with_multiple_files("src/dick", ["salome.py", "Rency.py"])
    )


# To help in debuging and printing errors faced during development.
PYTHONASYNCIODEBUG = 1
PYTHONTRACEMALOC = 1

if __name__ == "__main__":
    exit(run())

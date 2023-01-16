import asyncio
from .src.utils import check_os

platform_os = check_os()

# To help in debuging and printing errors faced during development.
PYTHONASYNCIODEBUG = 1
PYTHONTRACEMALOC = 1

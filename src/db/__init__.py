#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/8/30
# @File Name: __init__.py


import os
from urllib.request import urlretrieve
from src.config import Config

database = Config.database  # operator


def download_file(path: str):
    print("Downloading database file. Please wait...")
    file_url = "https://static.rtast.cn/data.sqlite"
    urlretrieve(file_url, path)  # standard lib for downloading file
    print("Download database file successfully.")


if database == "sqlite3":
    if not os.path.exists("./src/db/data.sqlite"):
        download_file("./src/db/data.sqlite")

if database == "sqlite3":
    from src.db.db import SQLite as Database
elif database == "deta":
    from src.db.db import DetaBase as Database
else:
    from src.db.db import MySQL as Database
__all__ = [Database]

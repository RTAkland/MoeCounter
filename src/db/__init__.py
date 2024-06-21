#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/8/30
# @File Name: __init__.py


import os
from urllib.request import urlretrieve

import requests

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
else:
    from src.db.db import VercelKV as Database

    base_url = "https://static.rtast.cn/static/counter"
    themes_file = [
        "lisu.json",
        "moebooru.json",
        "asoul.json",
        "blacked.json",
        "hgelbooru.json",
        "lewd.json",
        "rule34.json",
        "hmoebooru.json"
    ]
    for i in themes_file:
        result = requests.get(base_url + f"/{i}").json()
        print(f"{i}, Done!")
        Config.themes[i.replace(".json", "")] = result
__all__ = [Database]

#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/8/30
# @File Name: __init__.py


import os
import sqlite3 as operator
from urllib.request import urlretrieve
from src.config import Config
from src.db.db import SQLite as Database

database = Config.database

if not os.path.exists('./src/db/data.sqlite'):
    print('Downloading database file. Please wait...')
    file_url = 'https://static.rtast.cn/data.sqlite'
    urlretrieve(file_url, './src/db/data.sqlite')
    print('Download database file successfully.')

__all__ = [Database, operator]

#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/8/30
# @File Name: __init__.py


import os
from urllib.request import urlretrieve
from src.config import Config

database = Config.database

if database == 'sqlite':
    import sqlite3 as operator

    if not os.path.exists('./src/db/data.sqlite'):
        print('Downloading database file. Please wait...')
        file_url = 'https://static.rtast.cn/data.sqlite'
        urlretrieve(file_url, './src/db/data.sqlite')
        print('Download database file successfully.')
    from src.db.db import SQLite as Database
elif 'redis' in database:
    import redis as operator
    from src.db.db import Redis as Database
__all__ = [Database, operator]

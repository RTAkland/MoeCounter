#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/8/30
# @File Name: __init__.py


import os
from src.config import Config

database = Config.database

if database == 'sqlite':
    import sqlite3 as operator
    from src.utils.t_download import download

    if not os.path.exists('./src/db/data.sqlite'):
        download('https://markusjoe.github.io/static_file_hosting/static/counter/data.sqlite')
    from src.db.db import SQLite as Database
elif 'redis' in database:
    import redis as operator
    from src.db.db import Redis as Database
__all__ = [Database, operator]

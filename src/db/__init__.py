#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/8/30
# @File Name: __init__.py


import os
from src.config import Config

database = Config.database


def split_(origin: str, type_: int = 0) -> dict:
    """

    :param origin:
    :param type_: 0 -> Mysql
    :return:
    """
    origin = origin.split('://')[-1]
    host = origin.split('@')[-1].split('/')[0].split(':')[0]
    port = origin.split('@')[-1].split('/')[0].split(':')[1]
    if type_ == 0:  # Mysql
        database_ = origin.split('@')[-1].split('/')[-1]
        user = origin.split('@')[0].split(':')[0]
        password = origin.split('@')[0].split(':')[1]
        return {
            'host': host,
            'port': port,
            'database': database_,
            'user': user,
            'password': password
        }


if database == 'sqlite':
    import sqlite3 as operator
    from src.utils.t_download import download

    if not os.path.exists('./src/db/data.sqlite'):
        download('https://markusjoe.github.io/static_file_hosting/static/counter/data.sqlite')
    from src.db.db import SQLite as Database
else:
    import pymysql as operator

    result = split_(database)
    for k, v in zip(result.keys(), result.values()):
        os.environ[f"m_{k}"] = v
    from src.db.db import MySQL as Database

__all__ = [Database, operator]

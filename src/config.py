#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/9/11
# @File Name: config.py


import os


class Config:
    """
    database type. Default is sqlite
    database file path is "./src/db/data.sqlite", it is not exists, before you run server first
    remote sqlite file url is "https://pac.rtst.tech/static_file_hosting/static/counter/data.sqlite"
    you can download it manually
    if you want to use mysql then replace "mysql|[Username]:[password]@[host]:[port]/[database]" with "sqlite"
    example: mysql-root:114514@127.0.0.1:3306/homo
    """
    database = "sqlite"
    if 'sqlite' in database:
        os.environ['counter_db_type'] = 'sqlite'
    elif 'mysql' in database:
        os.environ['counter_db_type'] = 'mysql'

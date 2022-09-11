#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/8/30
# @File Name: __init__.py.py


from src.config import Config

if Config.database == 'sqlite':
    from src.db.db import SQLite as Database
else:
    from src.db.db import MySQL as Database


__all__ = [Database]

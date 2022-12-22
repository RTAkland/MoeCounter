#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/9/11
# @File Name: config.py
import os


class Config:
    """
    Available database:  sqlite3, mysql
    sqlite3 -> sqlite3   (default)
    mysql -> user:pwd@host:port/db
    """
    database = os.getenv('COUNTER_DB') or "sqlite3"  # Database type
    DETA = eval(os.getenv('DETA_RUNTIME').title())  # mark Deta

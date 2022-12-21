#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/9/11
# @File Name: config.py


class Config:
    """
    Available database:  sqlite3, mysql
    sqlite3 -> sqlite3   (default)
    mysql -> user:pwd@host:port/db
    """
    database = "sqlite3"  # Database type

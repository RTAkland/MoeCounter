#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/9/11
# @File Name: config.py
import os


class Config:
    """
    Available database:  sqlite3, mysql, detaBase
    sqlite3 -> sqlite3   (default)
    mysql -> mysql://user:pwd@host:port/db
    deta -> deta
    """
    database = os.getenv("COUNTER_DB") or "sqlite3"  # 数据库类型
    if os.getenv("PJ_DETA") is not None:
        database = "deta"  # 自动设置为deta

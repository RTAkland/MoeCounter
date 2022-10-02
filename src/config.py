#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/9/11
# @File Name: config.py

import os


class Config:
    """
    Available database: sqlite3, Redis.
    Redis: "redis://host:port@password".
        If your database doesn't have password, just don't type "@password".
        Don't type ":" to use default port.
    """
    database = "sqlite"  # Database type
    if 'redis' in database:
        os.environ['c_not_full'] = "True"  # Not full API supported.
        os.environ['c_host'] = database.split('://')[-1].split(':')[0]
        if ':' not in database.split('://'):
            os.environ['c_port'] = '6379'
        else:
            os.environ['c_port'] = database.split('://')[-1].split('@')[0].split(':')[-1]
        if '@' in database:
            os.environ['c_password'] = database.split('://')[-1].split(':')[-1].split('@')[-1]

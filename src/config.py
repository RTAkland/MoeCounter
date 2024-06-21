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
    database = os.getenv("COUNTER_DB") or "vercelkv"  # 数据库类型
    api_key = os.getenv("VERCEL_KV_KEY") or "<KEY>"
    vercel_kv_url = os.getenv("VERCEL_KV_URL") or "http://127.0.0.1:8000"
    themes = {}

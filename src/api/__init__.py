#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/9/2
# @File Name: __init__.py.py

from fastapi import APIRouter

api = APIRouter()

from src.api import view

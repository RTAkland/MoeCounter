#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/8/30
# @File Name: __init__.py


from src.main import main
from src.api import api
from fastapi import FastAPI


def create_app():
    """
    Create a app object
    :return:
    """
    app = FastAPI()
    app.include_router(main)
    app.include_router(api, prefix="/api")
    return app

#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/9/2
# @File Name: view.py


from src.api import api
from src.db import Database
from fastapi.responses import FileResponse


@api.get('/query/{name}')
async def query(name: str):
    times = Database().query(name)[1]
    return {name: times}


@api.get('/query-all/')
async def query_all(limit: int = 30):
    data = Database().query_all()[:limit]
    result = {}
    for i in data:
        result[i[0]] = i[1]
    return result


@api.get('/export/')
async def export():
    return FileResponse('./src/db/data.sqlite')


@api.get('/query-theme/{name}')
async def query_theme(name: str):
    themes = []
    for i in range(10):
        data = Database().query_image(name + '/' + str(i))[0]
        themes.append(data)
    return themes

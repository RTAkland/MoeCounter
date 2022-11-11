#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/9/2
# @File Name: view.py

import time

from src.api import api
from src.db import Database
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse


async def _time():
    return time.time()


@api.get('/query/{name}')
async def query(name: str):
    data = Database().query(name)
    response = {
        'code': 200,
        'time': await _time(),
        'data': {
            'name': data[0],
            'times': data[1]
        }
    }
    return response


@api.get('/query-all/')
async def query_all(limit: int = 30):
    data = Database().query_all()[:limit]
    response = {
        'code': 200,
        'time': await _time(),
        'data': []
    }
    for i in data:
        response['data'].append({
            'name': i[0],
            'times': i[1]
        })
    return response


@api.get('/export/')
async def export():
    return FileResponse('./src/db/data.sqlite')


@api.get('/query-theme/{name}')
async def query_theme(name: str):
    data = Database().query_image(name)
    response = {
        'code': 200,
        'time': await _time(),
        'data': []
    }
    for i in data:
        response['data'].append({
            'index': i[0],
            'image': i[1],
            'width': i[2],
            'height': i[3]
        })
    return JSONResponse(response)

#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/8/30
# @File Name: view.py


from src.main import main
from src.utils import resp
from fastapi import Request
from fastapi.responses import RedirectResponse
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

template = Jinja2Templates('./src/templates')


@main.get('/favicon.ico')
async def favicon():
    return FileResponse('./src/static/favicon.ico')


@main.get('/')
async def redirect_index():
    return RedirectResponse('/_redirect')


@main.get('/{name}')
async def index(req: Request, name: str, length: int = 7, theme: str = 'lewd'):
    if length > 10:
        return {'code': -200, 'msg': 'Length Error'}
    response = await resp(name, length, theme)

    return template.TemplateResponse('index.html',
                                     context={'request': req,
                                              'context': response['context'],
                                              'g_width': response['g_width'],
                                              'g_height': response['g_height']},
                                     headers=response['headers'])

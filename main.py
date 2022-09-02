#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/9/2
# @File Name: main.py


import uvicorn
from src import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')

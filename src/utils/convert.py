#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/8/30
# @File Name: convert.py


import os
import base64
import sqlite3
import asyncio


class SQLite:
    def __init__(self):
        self.conn = sqlite3.connect('../db/data.sqlite')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    async def insert(self, _id: str, b64: str, width: int, height: int) -> bool:
        self.cursor.execute('insert into image values ("%s", "%s", %s, %s)' % (_id, b64, width, height))
        return True


async def convert():
    dirs = os.listdir('../static')
    for i in dirs:
        files = os.listdir(f'../static/{i}')
        for b in files:
            with open(f'../static/{i}/{b}', 'rb') as fp:
                if i == 'moebooru':
                    width = 45
                    height = 100
                elif i == 'lewd':
                    width = 45
                    height = 100
                elif i == 'lisu':
                    width = 66
                    height = 152
                else:
                    width = 68
                    height = 150
                await SQLite().insert(f'{i}/{b}', base64.b64encode(fp.read()).decode('utf-8'), width, height)


asyncio.run(convert())

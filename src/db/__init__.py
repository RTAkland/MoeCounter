#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/8/30
# @File Name: __init__.py.py


import os
import sqlite3
from urllib.request import urlopen


class SQLite:
    def __init__(self):
        self.conn = sqlite3.connect('./src/db/data.sqlite')
        # self.conn = sqlite3.connect('./data.sqlite')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def query(self, _id: str) -> tuple:
        self.cursor.execute('select * from data where id="%s"' % _id)
        result = self.cursor.fetchone()
        if result is None:
            self.insert(_id)
            return tuple([_id, 0])
        self.update(_id, result[1])
        return result

    def insert(self, _id: str) -> bool:
        self.cursor.execute('insert into data (id, times) values ("%s", 0)' % _id)
        return True

    def update(self, _id: str, times: int) -> bool:
        times += 1
        self.cursor.execute('update data set times=%s where id="%s"' % (times, _id))
        return True

    def query_all(self) -> list:
        self.cursor.execute('select * from data')
        result = self.cursor.fetchall()
        return result

    def query_image(self, _id: str) -> list:
        self.cursor.execute('select * from image where id="%s"' % _id)
        result = self.cursor.fetchall()
        return result


if __name__ != '__main__':
    if not os.path.exists('./src/db/data.sqlite'):
        print('database file not exists, start downloading...')
        resp = urlopen('https://pac.rtst.tech/static_file_hosting/static/counter/data.sqlite').read()
        with open('./src/db/data.sqlite', 'wb') as fp:
            fp.write(resp)
        print('Done.')

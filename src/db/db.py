#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/9/11
# @File Name: db.py


import os
from src.db import operator


class Base:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __del__(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def query(self, _id: str) -> tuple:
        self.cursor.execute('select * from data where id="%s";' % _id)
        result = self.cursor.fetchone()
        if result is None:
            self.insert(_id)
            return tuple([_id, 0])
        self.update(_id, result[1])
        return result

    def insert(self, _id: str) -> bool:
        self.cursor.execute('insert into data (id, times) values (%s, 1);' % _id)
        return True

    def update(self, _id: str, times: int) -> bool:
        times += 1
        self.cursor.execute('update data set times=%s where id="%s";' % (times, _id))
        return True

    def query_all(self) -> list:
        self.cursor.execute('select * from data;')
        result = self.cursor.fetchall()
        return result

    def query_image(self, theme: str) -> list:
        self.cursor.execute('select * from %s;' % theme)
        result = self.cursor.fetchall()
        return result


class SQLite(Base):
    def __init__(self):
        super().__init__()
        self.conn = operator.connect('./src/db/data.sqlite')
        self.cursor = self.conn.cursor()

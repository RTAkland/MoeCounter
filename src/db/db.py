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


class Redis(Base):
    def __init__(self):
        super().__init__()
        self.host: str = os.getenv('c_host')
        self.port: int = int(os.getenv('c_port'))
        self.password: str = os.getenv('c_password')  # if is None then it is None. lol
        self.conn = operator.Redis(host=self.host,
                                   port=self.port,
                                   password=self.password,
                                   decode_responses=True)

    def __del__(self):
        self.conn.close()

    def query(self, _id: str) -> tuple:
        return self._get(_id)

    def insert(self, _id: str) -> bool:
        return self._set(_id)

    def update(self, _id: str, times: int) -> bool:
        return self._set(_id, times)

    def query_all(self) -> list:
        return self._get_all()

    def query_image(self, theme: str) -> list:
        return self._get_image(theme)

    def _get(self, _id: str) -> tuple:
        result = self.conn.get(_id)
        if result is None:
            self._set(_id)
            return tuple([_id, 0])
        self._set(_id, int(result))
        return tuple([_id, int(result)])

    def _set(self, _id: str, times: int = 0) -> bool:
        times += 1
        return self.conn.set(_id, times)

    def _get_all(self) -> list:
        results = self.conn.keys()
        return results

    def _get_image(self, theme: str) -> list:
        images = []
        for i in range(10):
            images.append([i, self.conn.get(f'{theme}-{i}')])
        width = int(self.conn.get(f'{theme}-width'))
        height = int(self.conn.get(f'{theme}-height'))
        for j in range(10):
            images[j].append(width)
            images[j].append(height)

        return images

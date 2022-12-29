#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/9/11
# @File Name: db.py


import os
from src.config import Config

if Config.database == 'sqlite3':
    import sqlite3 as operator
elif Config.database == 'deta':
    from deta import Deta
else:
    import pymysql as operator


class BaseSQL:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __del__(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    async def query(self, _id: str) -> tuple:
        self.cursor.execute('select * from data where id="%s";' % _id)
        result = self.cursor.fetchone()
        if result is None:
            await self.insert(_id)
            return tuple([_id, 0])
        await self.update(_id, result[1])
        return result

    async def insert(self, _id: str) -> bool:
        self.cursor.execute('insert into data (id, times) values ("%s", 1);' % _id)
        return True

    async def update(self, _id: str, times: int) -> bool:
        times += 1
        self.cursor.execute('update data set times=%s where id="%s";' % (times, _id))
        return True

    async def query_all(self) -> list:
        self.cursor.execute('select * from data;')
        result = self.cursor.fetchall()
        return result

    async def query_image(self, theme: str) -> list:
        self.cursor.execute('select * from %s;' % theme)
        result = self.cursor.fetchall()
        return result


class SQLite(BaseSQL):
    def __init__(self):
        super().__init__()
        self.conn = operator.connect('./src/db/data.sqlite')
        self.cursor = self.conn.cursor()


class MySQL(BaseSQL):
    def __init__(self):
        super().__init__()
        _CONFIG = Config.database.split('@')
        user = _CONFIG[0].split(':')[0]
        pwd = _CONFIG[0].split(':')[1]
        host = _CONFIG[1].split(':')[0]
        port = int(_CONFIG[1].split(':')[1].split('/')[0])
        db = _CONFIG[1].split('/')[1]

        self.conn = operator.connect(user=user,
                                     passwd=pwd,
                                     host=host,
                                     port=port,
                                     database=db)
        self.cursor = self.conn.cursor()


class DetaBase:
    def __init__(self):
        self.__deta = Deta(os.getenv("PJ_DETA"))
        self.__data = self.__deta.Base("times")
        self.__image = self.__deta.Base("images")

    async def __get(self, _id: str) -> tuple:
        result = self.__data.get(_id)
        if result is None:
            await self.__put_data(_id)
            return tuple([_id, 0])
        await self.update(_id, result["times"])
        return tuple([_id, result["times"]])

    async def __put_data(self, _id: str) -> bool:
        self.__data.put({"times": 0}, _id)
        return True

    async def __update_data(self, _id: str, times: int) -> bool:
        new = {"times": times + 1}
        self.__data.update(new, _id)
        return True

    async def __insert_data(self, _id: str) -> bool:
        await self.__put_data(_id)
        return True

    async def __get_images(self, theme: str) -> list:
        response = []
        result = self.__image.get(theme)
        try:
            for i in result:
                if i != "key":
                    response.append(tuple([
                        i,
                        result[i]["base64"],
                        result[i]["width"],
                        result[i]["height"]
                    ]))
        except TypeError:
            return []
        return response

    async def query(self, _id: str) -> tuple:
        result = await self.__get(_id)
        return result

    async def insert(self, _id: str) -> bool:
        await self.__insert_data(_id)
        return True

    async def update(self, _id: str, times: int) -> bool:
        await self.__update_data(_id, times)
        return True

    async def query_all(self) -> list:
        pass

    async def query_image(self, theme: str) -> list:
        result = await self.__get_images(theme)
        return result

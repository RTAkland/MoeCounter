#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/9/11
# @File Name: db.py
import requests

from src.config import Config

if Config.database in ["sqlite3", "sqlite"]:
    import sqlite3 as operator


class SQL:
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


class SQLite(SQL):
    def __init__(self):
        super().__init__()
        self.conn = operator.connect('./src/db/data.sqlite')
        self.cursor = self.conn.cursor()


class VercelKV:
    async def query(self, _id: str) -> tuple:
        times = requests.get(
            f"{Config.vercel_kv_url}/get/{_id}",
            headers={"Authorization": f"Bearer {Config.api_key}"}
        ).json()["result"]
        if times is None:
            await self.insert(_id)
            return tuple([_id, 0])
        await self.update(_id, int(times))
        return tuple([_id, times])

    async def insert(self, _id: str) -> bool:
        requests.get(
            f"{Config.vercel_kv_url}/set/{_id}/1",
            headers={"Authorization": f"Bearer {Config.api_key}"}
        )
        return True

    async def update(self, _id: str, times: int) -> bool:
        times += 1
        requests.get(
            f"{Config.vercel_kv_url}/set/{_id}/{times}",
            headers={"Authorization": f"Bearer {Config.api_key}"}
        )
        return True

    async def query_all(self) -> list:
        return list("")

    async def query_image(self, theme: str) -> list:
        return Config.themes[theme]

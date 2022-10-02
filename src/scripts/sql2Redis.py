#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/10/2
# @File Name: sql2Redis


import redis
import sqlite3

redis = redis.Redis('localhost')
sqlite = sqlite3.connect('./data.sqlite')
cursor = sqlite.cursor()

table = 'blacked'

cursor.execute('select * from %s;' % table)
data = cursor.fetchall()
for i in data:
    redis.set(f'{table}-{i[0]}', i[1])
redis.set(f'{table}-width', data[0][-2])
redis.set(f'{table}-height', data[0][-1])

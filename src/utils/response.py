#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/8/30
# @File Name: response.py


from src.db import Database


async def resp(_id: str, length: int = 7, theme: str = "lewd") -> dict:
    """
    generate dict response
    include all information
    :param _id: name
    :param length:  length for counter
    :param theme:  theme for counter
    :return:
    """
    result = await Database().query(_id)
    times = result[1]
    str_number = str(times)  # 将整形转换为字符串
    len_number = len(str_number)  # 再获取字符串长度
    g_length = length * "0"  # 根据输入的位数来生成0的数量
    show_number = str(g_length[:-len_number] + str_number)
    context = []
    headers = {"cache-control": "max-age=0, no-cache, no-store, must-revalidate",
               "Content-Type": "image/svg+xml; charset=utf-8"}
    data = await Database().query_image(theme)
    height = data[0]["height"]
    width = data[0]["width"]
    counter = 0
    for i, n in zip(data, show_number):
        context.append({
            "position": i["width"] * counter,
            "width": i["width"],
            "height": i["height"],
            "base64": data[int(n)]["base64"]
        })
        counter += 1

    return {
        "context": context,
        "g_width": length * width,
        "g_height": height,
        "headers": headers
    }

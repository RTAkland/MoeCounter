#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/8/30
# @File Name: response.py


from src.db import Database


async def resp(_id: str, length: int = 7, theme: str = 'lewd') -> dict:
    """
    return a response
    :param _id:
    :param length:
    :param theme:
    :return:
    """
    times = Database().query(_id)[1]
    str_number = str(times)  # 将整形转换为字符串
    len_number = len(str_number)  # 再获取字符串长度
    g_length = length * '0'  # 根据输入的位数来自动生成0的数量
    show_number = str(g_length[:-len_number] + str_number)
    context = []
    w_h = Database().query_image(theme + '/0')[0]
    count = 0  # 计数器, 每次遍历一次则加一, 让图片x轴相乘
    for i in show_number:
        data = Database().query_image(theme + '/' + i)[0]
        context.append({'position': data[-2] * count,
                        'width': data[-2],
                        'height': data[-1],
                        'base64': data[1]})
        count += 1
    headers = {'cache-control': 'max-age=0, no-cache, no-store, must-revalidate'}

    return {'context': context,
            'g_width': length * w_h[-2],
            'g_height': w_h[-1],
            'headers': headers}

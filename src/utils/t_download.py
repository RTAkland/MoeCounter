#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/9/3
# @File Name: t_download.py


import threading
import requests


class ThreadedDownload(threading.Thread):
    def __init__(self,
                 url: str,
                 filename: str,
                 thread_id: int,
                 start_seek: int,
                 end_seek: int,
                 offset: int
                 ):
        super().__init__()
        self.url = url
        self.filename = filename
        self.thread_id = thread_id
        self.start_seek = start_seek
        self.end_seek = end_seek
        self.offset = offset

    def download(self):
        resp = requests.get(self.url, headers={'Range': f'Bytes={self.start_seek}-{self.end_seek}'})
        with open('./src/db/data.sqlite', 'rb+') as fp:
            fp.seek(self.start_seek)
            fp.write(resp.content)

    def run(self) -> None:
        self.download()


def download(url: str, threads: int = 4) -> None:
    filename = url.split('/')[-1]
    open('./src/db/data.sqlite', 'wb').close()  # create an empty file
    head = requests.head(url)
    if head.status_code == 301:
        head = requests.head(head.headers['Location'])
    filesize = int(head.headers['Content-Length'])
    offset = filesize // threads
    start = 0
    for i in range(threads):
        end = offset + start
        ThreadedDownload(url, filename, i, start, end, offset).run()
        start = end



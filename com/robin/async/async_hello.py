#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 13:49
# @Author  : bin
# @Site    : 
# @File    : async_hello.py
# @Software: PyCharm Community Edition


import asyncio


@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:


loop = asyncio.get_event_loop()


# 执行coroutine
loop.run_until_complete(hello())
loop.close()
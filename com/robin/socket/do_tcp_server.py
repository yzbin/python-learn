#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 16:22
# @Author  : bin
# @Site    : 
# @File    : do_tcp_server.py
# @Software: PyCharm Community Edition

import socket
import threading
import time


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
# 创建socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
s.bind(('127.0.0.1', 10000))
s.listen(5)
print('Waiting for connetcion ...')

while True:
    # 接受一个新连接
    sock, addr= s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

































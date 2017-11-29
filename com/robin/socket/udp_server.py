#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 17:24
# @Author  : bin
# @Site    : 
# @File    : udp_server.py
# @Software: PyCharm Community Edition

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 10001))
print('Bind UDP on 10001')
while True:
    data, addr =s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)







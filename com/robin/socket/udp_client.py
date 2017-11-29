#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 17:25
# @Author  : bin
# @Site    : 
# @File    : udp_client.py
# @Software: PyCharm Community Edition

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarch']:
    s.sendto(data, ('127.0.0.1', 10001))
    print(s.recv(1024).decode('utf-8'))
s.close()

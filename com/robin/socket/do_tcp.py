#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 17:07
# @Author  : bin
# @Site    : 
# @File    : do_tcp.py
# @Software: PyCharm Community Edition

# # 创建socket：
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 建立连接
# s.connect(('www.sina.com.cn', 80))
#
# # 发送数据
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
#
# # 接受数据
# buffer = []
# while True:
#     b = s.recv(1024)
#     if b:
#         buffer.append(b)
#     else:
#         break
# data = b''.join(buffer)
#
# # 关闭连接：
# s.close()
#
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
#
# # 把接受到的数据写入文件
# with open('sina.html', 'wb') as f:
#     f.write(html)
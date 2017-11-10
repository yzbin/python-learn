#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/10 10:29
# @Author  : bin
# @Site    : 
# @File    : Demo1.py
# @Software: PyCharm Community Edition

#在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，
# 所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
# 然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
# try:
#     f = open('a.txt', 'r')
#     # f = open(r'\Users\admin\PycharmProjects\python-learn\com\centchain\io\a.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# with open('a.txt', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())     # 把末尾的'\n'删掉


# with open('a.jpg', 'rb') as f:
#     for line in f.readlines():
#         print(line.strip())       # 把末尾的'\n'删掉

# with open('gbk.txt', encoding='utf-8') as f:
#     print(f.read())

# with open('hello.txt', 'w+') as f:
#     print(f.write('hello robin'))













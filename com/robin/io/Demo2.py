#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/10 13:22
# @Author  : bin
# @Site    : 
# @File    : Demo2.py
# @Software: PyCharm Community Edition


# 很多时候，数据读写不一定是文件，也可以在内存中读写。
#
# StringIO顾名思义就是在内存中读写str。
#
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可

# from io import StringIO
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world!')
# print(f.getvalue())

# from io import StringIO
# f = StringIO('Hello!\nHi\nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())

# from io import BytesIO
# f = BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

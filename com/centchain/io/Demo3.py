#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/10 13:25
# @Author  : bin
# @Site    : 
# @File    : Demo3.py
# @Software: PyCharm Community Edition

import os
print(os.name)  # 操作系统类型

# 改方法只适用于linux系统
# print(os.uname())  # 详细的系统信息

# 环境变量
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
# print(os.environ)
#
# # 要获取某个环境变量的值，可以调用os.environ.get('key')：
# print(os.environ.get('PATH'))


# 操作文件和目录
#
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
print(os.path.abspath('.'))   # 查看当前目录的绝对路径

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
print(os.path.join(r'C:\Users\admin\PycharmProjects\python-learn\com\centchain\io', 'test'))

# os.mkdir(r'C:\Users\admin\PycharmProjects\python-learn\com\centchain\io\test')

os.rmdir(r'C:\Users\admin\PycharmProjects\python-learn\com\centchain\io\test')

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
# 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：


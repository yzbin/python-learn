#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/25 11:54
# @Author  : robin
# @Site    : 
# @File    : Demo1.py
# @Software: PyCharm Community Edition


# print(abs(-10))
# print(abs)
#
# x = abs(-10)
# print(x)
#
# f = abs
# print(f)
#
# print(f(-10))


# abs = 10
# print(abs(-10))

# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。


# a simple example

def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))

# 编写高阶函数，就是让函数的参数能够接收别的函数。



















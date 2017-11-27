#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 19:31
# @Author  : bin
# @Site    : 
# @File    : special_getitem.py
# @Software: PyCharm Community Edition


class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


f = Fib()
print(f[0])
print(f[2])
print(f[3])
print(f[10])
print(f[100])








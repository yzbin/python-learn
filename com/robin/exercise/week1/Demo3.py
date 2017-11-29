#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 9:36
# @Author  : bin
# @Site    : 
# @File    : Demo3.py
# @Software: PyCharm Community Edition

# (3)九九乘法表输出。工整打印输出常用的九九乘法表，格式不限。
for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={:2} ".format(j, i, i*j), end='')
    print('')


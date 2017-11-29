#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 9:55
# @Author  : bin
# @Site    : 
# @File    : Demo4.py
# @Software: PyCharm Community Edition

# (4)阶乘计算。计算1+2!+3!+...+10!
sum = 0
tmp = 1
for i in range(1, 11):
    tmp *= i
    sum += tmp
print("运算的结果是:{}".format(sum))






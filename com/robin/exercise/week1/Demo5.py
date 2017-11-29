#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 10:07
# @Author  : bin
# @Site    : 
# @File    : Demo5.py
# @Software: PyCharm Community Edition

# (5)猴子吃桃问题
n = 1
for i in range(5, 0, -1):
    n = (n+1) << 1
print(n)


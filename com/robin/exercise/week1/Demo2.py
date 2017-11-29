#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 9:26
# @Author  : bin
# @Site    : 
# @File    : Demo2.py
# @Software: PyCharm Community Edition

# (2)整数序列求和。用户输入一个正整数N,计算从1到N(包含1和N)相加之后的结果
n = input("请输入整数N:")
sum = 0
for i in range(int(n)):
    sum += i+1
print("1 到 %s 的求和结果 %s" % (n, sum))

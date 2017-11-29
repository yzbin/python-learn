#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 10:17
# @Author  : bin
# @Site    : 
# @File    : Demo7.py
# @Software: PyCharm Community Edition

# (7)五角星的绘制。绘制一个红色的五角星

from turtle import *

fillcolor("red")
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos()) < 1:
        break
end_fill()












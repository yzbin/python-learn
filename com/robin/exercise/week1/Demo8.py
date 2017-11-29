#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 17:53
# @Author  : bin
# @Site    : 
# @File    : Demo8.py
# @Software: PyCharm Community Edition

# 太阳花的绘制。绘制一个太阳花的图形，如图所示。
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()




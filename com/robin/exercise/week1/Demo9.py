#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 17:58
# @Author  : bin
# @Site    : 
# @File    : Demo9.py
# @Software: PyCharm Community Edition

# 螺旋线绘制
import turtle
import time
turtle.speed('fastest')
turtle.pensize(2)
for x in range(100):
    turtle.forward(2*x)
    turtle.left(90)
time.sleep(3)





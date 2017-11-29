#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 10:10
# @Author  : bin
# @Site    : 
# @File    : Demo6.py
# @Software: PyCharm Community Edition

# 健康食谱输出。列出5种不同的食材，请输出它们有组成的所有菜式名称
diet = ['西红柿', '花椰菜', '黄瓜', '牛排', '虾仁']
for x in range(0, 5):
    for y in range(0, 5):
        if not (x == y):
            print("{}{}".format(diet[x], diet[y]))







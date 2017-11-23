#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 0:08
# @Author  : robin
# @Site    : 
# @File    : Demo4.py
# @Software: PyCharm Community Edition

d = {'MIchael': 95, 'Bob': 75, 'Tracy': 85}
print(d['MIchael'])

d['Adam'] = 67
print(d['Adam'])

d['Jack'] = 90
print(d['Jack'])

d['Jack'] = 88
print(d['Jack'])

print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thoms', -1))

print(d.pop('Bob'))

s = set([1, 2, 3])
print(s)









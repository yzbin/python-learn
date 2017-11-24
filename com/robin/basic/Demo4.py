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

s = set([1, 1, 2, 2, 3, 3])
print(s)


s.add(4)
print(s)

s.remove(4)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])


print(s1 & s2)

print(s1 | s2)

key = [1, 2, 3, 4, 5]

# d[key] = 'a list'


s1 = set(key)

print(s1)


a = ['c', 'b', 'a']
a.sort()
print(a)

a = 'abc'
b = a.replace('a', 'A')
print(a)
print(b)
































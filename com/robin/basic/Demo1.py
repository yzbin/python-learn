#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/23 23:14
# @Author  : robin
# @Site    :
# @File    : Demo1.py
# @Software: PyCharm Community Edition

classmates = ['Michael', 'Bob' , 'Tracy']
print(classmates)

print(len(classmates))

print(classmates[0])
print(classmates[1])
print(classmates[2])
# print(classmates[3])


print(classmates[-1])
print(classmates[-2])


classmates.append('Adam')
print(classmates)

classmates.insert(1, 'Jack')

classmates.pop()

print(classmates)

classmates.pop(1)

print(classmates)

classmates[1] = 'Sarah'

print(classmates)


L = ['Apple', 123, True]
print(L)

s = ['python', 'java', ['asp', 'php'], 'scheme']

print(len(s))

classmates = ('Michael', 'Bob', 'Tracy')

t = (1)
print(t)

t = (1,)

print(t)


t = ('a', 'b', ['A', 'B'])
print(t[2][0])
print(t[2][1])


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])























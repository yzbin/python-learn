#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/26 18:43
# @Author  : robin
# @Site    : 
# @File    : Demo2.py
# @Software: PyCharm Community Edition


# def f(x):
#     return x * x
#
#
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r))
#
#
# L = []
# for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     L.append(f(n))
# print(L)
#
# print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#
#
# from functools import reduce
#
#
# def add(x, y):
#     return x + y
#
#
# print(reduce(add, [1, 3, 5, 7, 9]))


# from functools import reduce
#
#
# def fn(x, y):
#     return x * 10 + y
#
#
# print(reduce(fn, [1, 3, 5, 7, 9]))


# from functools import reduce
#
#
# def fn(x, y):
#     return x * 10 + y
#
#
# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
#
# print(reduce(fn, map(char2num, '13579')))

#
# from functools import reduce
#
#
# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
#
# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# def normalize(name):
#     return name[:1].upper() + name[1:].lower()
#
#
# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

from functools  import reduce


def prod(L):
    return reduce(lambda x, y: x*y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')






































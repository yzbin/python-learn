#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 22:16
# @Author  : robin
# @Site    : 
# @File    : Demo4.py
# @Software: PyCharm Community Edition


# L = []
# n = 1
# while n <= 99:
#     L.append(n)
#     n = n + 2
#
# print(L)

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print([L[0], L[1], L[2]])
#
# r = []
# n = 3
# for i in range(n):
#     r.append(L[i])
#
# print(r)
#
# print(L[:3])
# print(L[1:3])
# print(L[-2:])
# print(L[-2:-1])

# L = list(range(100))
# print(L)
# print(L[:10])
# print(L[10:])
# print(L[10:20])
# print(L[:10:2])
# print(L[::5])
# print(L[:])


# print((0, 1, 2, 3, 4, 5)[:3])
#
# print('ABCDEFG'[:3])
# print('ABCDEFG'[::2])

# L = ['Beijing', 'shanghai', 'guangzhou']
#
# for i in L:
#     print(i)

# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key)
#
# for value in d.values():
#     print(value)
#
# for k, v in d.items():
#     print(k, v)

# for ch in 'ABC':
#     print(ch)
#
# from collections import Iterable
#
#
# print(isinstance('abc', Iterable))
# print(isinstance([1, 2, 3], Iterable))
# print(isinstance(123, Iterable))

# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)
#
#
# for x, y in [(1, 1), (2, 4), (3, 9)]:
#     print(x, y)


# print(list(range(1, 11)))
#
# L = []
# for x in range(1, 11):
#     L.append(x*x)
# print(L)
#
# print([x*x for x in range(1, 11)])
#
# print([x*x for x in range(1, 11) if x % 2 ==0 ])

# print([m+n for m in 'ABC' for n in 'XYZ'])
#
# import os
# print([d for d in os.listdir('.')])


# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# for k, v in d.items():
#     print(k, '=', v)

# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])
#
#
# L1 = ['Hello', 'World', 18, 'Apple', None]
#
# L2 = [ x for x in L1 if isinstance(x, str)]
# print(L2)


# L = [x * x for x in range(10)]
# print(L)
# g = (x * x for x in range(10))
# print(g)
#
# for i in g:
#     print(i)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# print(fib(6))


def fib1 (max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib1(6))


# def odd():
#     print('step1')
#     yield 1
#     print('step2')
#     yield (2)
#     print('step3')
#     yield (5)
#
#
# o = odd()
# print(next(o))
# print(next(0))
# print(next(o))
# print(next(o))


# for n in fib1(6):
#     print(n)

g = fib1(6)

while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break

















































































































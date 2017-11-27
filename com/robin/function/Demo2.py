#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 10:39
# @Author  : bin
# @Site    : 
# @File    : Demo2.py
# @Software: PyCharm Community Edition

# import math
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
#
#
# print(abs(-99))
#
#
# def nop():
#     pass
#
#
# age = 0
# if age >= 18:
#     pass
#
# # print(my_abs('A'))
#
#
# # print(abs('A'))
#
#
# # print(my_abs('A'))
#
#
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
#
#
# x, y = move(100, 100, 60, math.pi/6)
# print(x, y)
#
#
# def power(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return
#
#
# # print(pow(5))
# # print(pow(15))
#
#
# print(pow(5, 2))
# print(pow(5, 3))
#
#
# # 默认参数
# def power1(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
#
# def enroll(name, gender, age =6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
#
#
# print(enroll('Sarah', 'F'))
# print(enroll('Adam', 'M', city='Tianjin'))
# print(enroll('Bob', 'M', 7))
#
#
# def add_end(L=[]):
#     L.append('END')
#     return L
#
#
# print(add_end([1, 2, 3, 4]))
# print(add_end(['x', 'y', 'z']))
#
# print(add_end())
# print(add_end())
# print(add_end())
# # 定义默认参数要牢记一点：默认参数必须指向不变对象！
#
#
# def add_end1(L=None):
#     if L is None:
#        L = []
#     L.append('END')
#     return L
#
#
# print(add_end1())
# print(add_end1())
#
#
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
#
# print(calc([1, 2, 3]))
# print(calc((1, 3, 5, 7)))
#
#
# # 可变参数
#
# def calc1(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
#
# print(calc1(1, 2))
# print(calc1())
#
# nums = [1, 2, 3]
# print(calc1(nums[0], nums[1], nums[2]))
#
# print(calc1(*nums))
#

# 关键字参数


# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
#
# print(person('Michael', 30))
# print(person('Bob', 35, city='Beiing'))
# print(person('Adam', 45, gender='M', job='Engineer'))
#
#
# extra = {'city': 'Beijing', 'job': 'Enginner'}
# print(person('Jack', 24, city=extra['city'], job=extra['job']))
#
# print(person('Jack', 24, **extra))


# 命名关键字参数

# def person1(name, age, **kw):
#     if 'city' in kw:
#         pass
#     if 'job' in kw:
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)

# 但是调用者仍可以传入不受限制的关键字参数：


# print(person1('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=12345))


# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
# def person2(name, age, *, city, job):
#     print(name, age, city, job)
#
#
# print(person2('Jack', 24, city='Beijing'))


# def person3(name, age, *args, city, job):
#     print(name, age, args, city, job)
#
#
# print(person3('Jack', 24, 'Beijing', 'Engineer'))

# def person4(name, age, *, city='Beijing', job):
#     print(name, age, city, job)
#
#
# print(person4('Jack', 24, job='Engineer'))


#
# Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
#
# 比如定义一个函数，包含上述若干种参数


# def f1(a, b, c=0, *args, **kw):
#     print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)
#
#
# def f2(a, b, c=0, *, d, **kw):
#     print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)
#
#
# print(f1(1, 2))
# print(f1(1, 2, 3))
# print(f1(1, 2, 3, 'a', 'b'))
# print(f1(1, 2, 3, 'a', 'b', x=99))


# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
#
# print(fact(1))
# print(fact(5))
# print(fact(100))
# print(fact(1000))


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num*product)











































































#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/26 23:14
# @Author  : robin
# @Site    : 
# @File    : decorator.py
# @Software: PyCharm Community Edition


# def now():
#     print('2015-3-24')
#
#
# f = now
# print(f())
#
# # 函数对象有一个__name__属性，可以拿到函数的名字
# print(now.__name__)
# print(f.__name__)

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。


def log(func):
    def wrraper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrraper

# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 我们要借助Python的@语法，把decorator置于函数的定义处

@log
def now():
    print('2017-11-26')


print(now())








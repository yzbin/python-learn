#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 19:06
# @Author  : bin
# @Site    : 
# @File    : special_iter.py
# @Software: PyCharm Community Edition

# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self   # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:   # 退出循环的条件
            raise StopIteration
        return self.a  # 返回下一个值


for n in Fib():
    print(n)


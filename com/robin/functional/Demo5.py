#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/26 22:51
# @Author  : robin
# @Site    : 
# @File    : Demo5.py
# @Software: PyCharm Community Edition

# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便

# 在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，
# 除了定义一个f(x)的函数外，还可以直接传入匿名函数：
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# 通过对比可以看出，匿名函数lambda x: x * x实际上就是:


# def f(x):
#     return x * x

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

# 匿名函数有个好处，因为函数没有名字，不必担心5cx函数名冲突
# 此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：


f = lambda x: x * x
print(f)
print(f(5))



def build(x, y):
    return lambda: x * x + y * y


# 请用匿名函数改造下面的代码：
#
# def is_odd(n):
#     return n % 2 == 1
#
#
# L = list(filter(is_odd, range(1, 20)))

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)








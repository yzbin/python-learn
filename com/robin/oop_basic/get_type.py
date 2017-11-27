#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 15:13
# @Author  : bin
# @Site    : 
# @File    : get_type.py
# @Software: PyCharm Community Edition

# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
# 使用type()

print(type(123))
print(type('str'))
print(type(None))

print(type(abs))


# 但是type()函数返回的是什么类型呢？它返回对应的Class类型。
# 如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同


print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：

import types


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)


# 使用isinstance()
#
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# 我们回顾上次的例子，如果继承关系是

# object -> Animal -> Dog -> Husky
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))


# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”



















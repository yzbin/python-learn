#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 15:38
# @Author  : bin
# @Site    : 
# @File    : attrs.py
# @Software: PyCharm Community Edition

# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，
# 它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
print(dir('abc'))


# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
# 它自动去调用该对象的__len__()方法，所以，下面的代码是等价的
print(len('ABC'))
print('ABC'.__len__())

# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法


class MyDog(object):
    def __len__(self):
        return 100


dog = MyDog()
print(len(dog))


# 剩下的都是普通属性或方法，比如lower()返回小写的字符串
print('ABC'.lower())


# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)

# 如果试图获取不存在的属性，会抛出AttributeError的错误
# print(getattr(obj, 'z'))  # 获取属性 'z'


# 可以传入一个default参数，如果属性不存在，就返回默认值

print(getattr(obj, 'z', 404))


# 也可以获得对象的方法
print(hasattr(obj, 'power'))  # 有属性'power'吗?

print(getattr(obj, 'power'))  # 获取属性 'power'

fn = getattr(obj, 'power')  # 获取属性 'power'并赋值到变量fn

print(fn)
print(fn())


# 小结
# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。
# 要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写
# sum = obj.x + obj.y
# 就不要写：
# sum = getattr(obj, 'x') + getattr(obj, 'y')


# 一个正确的用法的例子如下：
# def readImage(fp):
#     if hasattr(fp, 'read'):
#         return readData(fp)
#     return None






#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 22:26
# @Author  : robin
# @Site    : 
# @File    : create_class_on_the_fly.py
# @Software: PyCharm Community Edition

# type()
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
# 比方说我们要定义一个Hello的class，就写一个hello.py模块


# 当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象，测试如下

# from com.robin.oop_advance.hello import Hello
#
# h = Hello()
# print(h.hello())
# print(type(Hello))
# print(type(h))

# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello
# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。


def fn(self, name='world'):
    print('Hello, %s' % name)


Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
h = Hello()
print(h.hello())


# 要创建一个class对象，type()函数依次传入3个参数：
#
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
# 仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。





















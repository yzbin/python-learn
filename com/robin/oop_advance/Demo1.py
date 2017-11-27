#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 17:49
# @Author  : bin
# @Site    : 
# @File    : Demo1.py
# @Software: PyCharm Community Edition


# 继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能。
#
# 回忆一下Animal类层次的设计，假设我们要实现以下4种动物：
#
# Dog - 狗狗；
# Bat - 蝙蝠；
# Parrot - 鹦鹉；
# Ostrich - 鸵鸟。
# 如果按照哺乳动物和鸟类归类，我们可以设计出这样的类的层次：

# 正确的做法是采用多重继承。首先，主要的类层次仍按照哺乳类和鸟类设计


class Animal(object):
    pass


# 大类
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass

# 现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类


class Runnable(object):
    def run(self):
        print('Running ...')


class Flyable(object):
    def fly(self):
        print('Flying ...')


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass

# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。

# Mixin
#
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。
# 这种设计通常称之为Mixin

# 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。
# 类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn

# 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。
# 类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn：


class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
#
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，
# 我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

# 这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。

# 由于Python允许使用多重继承，因此，Mixin就是一种常见的设计。
#
# 只允许单一继承的语言（如Java）不能使用Mixin的设计




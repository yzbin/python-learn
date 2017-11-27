#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 16:35
# @Author  : bin
# @Site    : 
# @File    : use_slots.py
# @Software: PyCharm Community Edition


# class Student(object):
#     pass
#
# # 然后，尝试给实例绑定一个属性：
#
#
# s = Student()
# s.name = 'robin'
# print(s.name)
#
# # 然后，尝试给实例绑定一个属性：
#
#
# # def set_age(self, age):  # 定义一个函数作为实例方法
# #     self.age = age
#
#
# # from types import MethodType
# # s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
# # s.set_age(25)     # 调用实例方法
# # print(s.age)      # 测试结果
#
# # 但是，给一个实例绑定的方法，对另一个实例是不起作用的
# #
# # s2 = Student()  # 创建新的实例
# # s2.set_age(25)  # 尝试调用方法
#
# # 为了给所有实例都绑定方法，可以给class绑定方法
#
#
# def set_score(self, score):
#     self.score = score
#
#
# Student.set_score = set_score
# # 给class绑定方法后，所有实例均可调用
#
# s.set_score(100)
# print(s.score)
#
# s2 = Student()
# s2.set_score(99)
# print(s2.score)

# 通常情况下，上面的set_score方法可以直接定义在class中，
# 但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现

# 使用__slots__
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性

class Student(object):
    __slots__ = ('name', 'age')   # 用tuple定义允许绑定的属性名称


# s = Student()   # 创建新的实例
# s.name = 'robin'  # 绑定属性'name'
# s.age = 25  # 绑定属性'age
# s.score = 99  # 绑定属性'score'

# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误


class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 9999


# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__







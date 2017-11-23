#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/23 23:36
# @Author  : robin
# @Site    : 
# @File    : Demo2.py
# @Software: PyCharm Community Edition

age = 20
if age >= 18:
    print('your age is ', age)
    print('adult')


age = 3
if age >= 18:
    print('your age is ', age)
else:
    print('your age is', age)
    print('teenager')


age = 3
if age >= 18:
    print('adult')
elif age >=6:
    print('teenager')
else:
    print('kid')


age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

s = input('birth:')
birth = int(s)
if birth < 2000:
    print("00前")
else:
    print('00后')


height = 1.75
weight = 80.5

bmi = weight/(height*height)
if bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi <28:
    print("肥胖")
else:
    print("严重肥胖")










#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 9:51
# @Author  : bin
# @Site    : 
# @File    : Demo0.py
# @Software: PyCharm Community Edition

a = 100

if a >= 0:
    print(a)
else:
    print(-a)

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'))

print(ord('中'))

print(chr(66))

print(chr(25991))

print('\u4e2d\u6587')

#
# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
#
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。
#
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：

print('ABC'.encode('ascii'))

print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：

print('Age: %s. Gender: %s' % (25, True))
# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：

print('growth rate: %d %%' % 7)

# 练习
#
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
# s1 = 72
# s2 = 85
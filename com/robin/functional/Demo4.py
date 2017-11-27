#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/26 22:12
# @Author  : robin
# @Site    : 
# @File    : Demo4.py
# @Software: PyCharm Community Edition


# 排序算法

# 排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，
# 因此，比较的过程必须通过函数抽象出来。

print(sorted([36, 5, -12, 9, -21]))

# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21], key=abs))


# 再看一个字符串排序的例子
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。

# 现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，
# 只要我们能用一个key函数把字符串映射为忽略大小写排序即可。
# 忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))


# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 请用sorted()对上述列表分别按名字排序：


def by_name(t):
    return t[0]


print(sorted(L, key=by_name))

# 再按成绩从高到低排序：


def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score, reverse=True)
print(L2)

















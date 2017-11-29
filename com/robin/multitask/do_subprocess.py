#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 10:45
# @Author  : bin
# @Site    : 
# @File    : do_subprocess.py
# @Software: PyCharm Community Edition

# 进程
#
# 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
#
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
#
# 下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的


import subprocess

print('$ nslookup www.pythonorg')
r = subprocess.call(['nslooup', 'www.python.org'])
print('Exit code:', r)




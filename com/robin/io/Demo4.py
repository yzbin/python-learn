#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 18:40
# @Author  : robin
# @Site    : 
# @File    : Demo4.py
# @Software: PyCharm Community Edition

import pickle
d = dict(name='bob', age='20', score=88)
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

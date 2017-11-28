#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/28 11:30
# @Author  : bin
# @Site    : 
# @File    : mydict.py
# @Software: PyCharm Community Edition


class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"Dict' object has not attribute %s" % key)

    def __setattr__(self, key, value):
        self[key] = value


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/28 11:13
# @Author  : bin
# @Site    : 
# @File    : do_logging.py
# @Software: PyCharm Community Edition


# logging
#
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
# 当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
# 这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件

# 写程序最痛苦的事情莫过于调试，程序往往会以你意想不到的流程来运行，你期待执行的语句其实根本没有执行，
# 这时候，就需要调试了。

# 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器






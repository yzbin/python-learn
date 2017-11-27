#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 23:40
# @Author  : robin
# @Site    : 
# @File    : orm.py
# @Software: PyCharm Community Edition

# ORM全称“Object Relational Mapping”，
# 即对象-关系映射，就是把关系数据库的一行映射为一个对象，
# 也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

# 让我们来尝试编写一个ORM框架。

# 编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，
# 想定义一个User类来操作对应的数据库表User，我们期待他写出这样的代码：

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
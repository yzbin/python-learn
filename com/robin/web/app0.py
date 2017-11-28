#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/28 15:12
# @Author  : bin
# @Site    : 
# @File    : app0.py
# @Software: PyCharm Community Edition

# Flask通过Python的装饰器在内部自动地把URL和函数给关联起来，所以，我们写出来的代码就像这样

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def singin_form():
    return '''
            <form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
            </form> '''


@app.route('/signin', methods=['POST'])
def sigin():
    # 需要从request对象读取表单内容
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password</h3>'


if __name__ == '__main__':
    app.run()







#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/28 15:53
# @Author  : bin
# @Site    : 
# @File    : app.py
# @Software: PyCharm Community Edition

from flask import Flask, request, render_template

# 只是因为Python支持关键字参数，很多Web框架允许传入关键字参数，然后，在框架内部组装出一个dict作为Model。
# 现在，我们把上次直接输出字符串作为HTML的例子用高端大气上档次的MVC模式改写一下

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def singnin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password =='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username = username)


if __name__ == '__main__':
    app.run()

# 通过MVC，我们在Python代码中处理M：Model和C：Controller，而V：View是通过模板处理的，
# 这样，我们就成功地把Python代码和HTML代码最大限度地分离了。

# 使用模板的另一大好处是，模板改起来很方便，而且，改完保存后，刷新浏览器就能看到最新的效果，
# 这对于调试HTML、CSS和JavaScript的前端工程师来说实在是太重要了。

# 在Jinja2模板中，我们用{{ name }}表示一个需要替换的变量。很多时候，还需要循环、条件判断等指令语句，
# 在Jinja2中，用{% ... %}表示指令。

# 比如循环输出页码：
#
# {% for i in page_list %}
#     <a href="/page/{{ i }}">{{ i }}</a>
# {% endfor %}
# 如果page_list是一个list：[1, 2, 3, 4, 5]，上面的模板将输出5个超链接。
# 有了MVC，我们就分离了Python代码和HTML代码。HTML代码全部放到模板里，写起来更有效率



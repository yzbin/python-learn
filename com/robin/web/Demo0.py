#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/28 14:44
# @Author  : bin
# @Site    : 
# @File    : Demo0.py
# @Software: PyCharm Community Edition


# 了解了HTTP协议和HTML文档，我们其实就明白了一个Web应用的本质就是：

# 1.浏览器发送一个HTTP请求；

# 2.服务器收到请求，生成一个HTML文档；

# 3.服务器把HTML文档作为HTTP响应的Body发送给浏览器；

# 4.浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

# 所以，最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。
# Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的。

# 如果要动态生成HTML，就需要把上述步骤自己来实现。不过，接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，
# 如果我们自己来写这些底层代码，还没开始写动态HTML呢，就得花个把月去读HTTP规范。

# 正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。
# 因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口，让我们专心用Python编写Web业务。

# 这个接口就是WSGI：Web Server Gateway Interface。
# WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。我们来看一个最简单的Web版本的“Hello, web!”




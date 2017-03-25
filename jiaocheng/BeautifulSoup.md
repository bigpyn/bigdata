在前面的例子用，我用了BeautifulSoup来从58同城抓取了手机维修的店铺信息，这个库使用起来的确是很方便的。本文是BeautifulSoup 的一个详细的介绍，算是入门把。文档地址：http://www.crummy.com/software/BeautifulSoup/bs4/doc/

什么是BeautifulSoup？

Beautiful Soup 是用Python写的一个HTML/XML的解析器，它可以很好的处理不规范标记并生成剖析树(parse tree)。 它提供简单又常用的导航（navigating），搜索以及修改剖析树的操作。它可以大大节省你的编程时间。

直接看例子：

#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

"""

soup = BeautifulSoup(html_doc)

print soup.title

print soup.title.name

print soup.title.string

print soup.p

print soup.a

print soup.find_all('a')

print soup.find(id='link3')

print soup.get_text()

结果为：

<title>The Dormouse's story</title>
title
The Dormouse's story
<p class="title"><b>The Dormouse's story</b></p>
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

The Dormouse's story
The Dormouse's story
Once upon a time there were three little sisters; and their names were
Elsie,
Lacie and
Tillie;
and they lived at the bottom of a well.
...

可以看出：soup 就是BeautifulSoup处理格式化后的字符串，soup.title 得到的是title标签，soup.p  得到的是文档中的第一个p标签，要想得到所有标签，得用find_all

函数。find_all 函数返回的是一个序列，可以对它进行循环，依次得到想到的东西.

get_text() 是返回文本,这个对每一个BeautifulSoup处理后的对象得到的标签都是生效的。你可以试试 print soup.p.get_text()

其实是可以获得标签的其他属性的，比如我要获得a标签的href属性的值，可以使用 print soup.a['href'],类似的其他属性，比如class也是可以这么得到的（soup.a['class']）。

特别的，一些特殊的标签，比如head标签，是可以通过soup.head 得到，其实前面也已经说了。

如何获得标签的内容数组？使用contents 属性就可以 比如使用 print soup.head.contents，就获得了head下的所有子孩子，以列表的形式返回结果，

可以使用 [num]  的形式获得 ,获得标签，使用.name 就可以。

获取标签的孩子，也可以使用children，但是不能print soup.head.children 没有返回列表，返回的是 <listiterator object at 0x108e6d150>,

不过使用list可以将其转化为列表。当然可以使用for 语句遍历里面的孩子。

关于string属性，如果超过一个标签的话，那么就会返回None，否则就返回具体的字符串print soup.title.string 就返回了 The Dormouse's story

超过一个标签的话，可以试用strings

向上查找可以用parent函数，如果查找所有的，那么可以使用parents函数

查找下一个兄弟使用next_sibling,查找上一个兄弟节点使用previous_sibling,如果是查找所有的，那么在对应的函数后面加s就可以

如何遍历树？

　使用find_all 函数

find_all(name, attrs, recursive, text, limit, **kwargs)

举例说明：

print soup.find_all('title')
print soup.find_all('p','title')
print soup.find_all('a')
print soup.find_all(id="link2")
print soup.find_all(id=True)

返回值为：

[<title>The Dormouse's story</title>]
[<p class="title"><b>The Dormouse's story</b></p>]
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
[<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

通过css查找,直接上例子把：

print soup.find_all("a", class_="sister")
print soup.select("p.title")

通过属性进行查找
print soup.find_all("a", attrs={"class": "sister"})

通过文本进行查找
print soup.find_all(text="Elsie")
print soup.find_all(text=["Tillie", "Elsie", "Lacie"])

限制结果个数
print soup.find_all("a", limit=2)

结果为：

[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
[<p class="title"><b>The Dormouse's story</b></p>]
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
[u'Elsie']
[u'Elsie', u'Lacie', u'Tillie']
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

总之，通过这些函数可以查找到想要的东西。

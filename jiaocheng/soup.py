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
print soup.find_all('title')
print soup.find_all('p','title')
print soup.find_all('a')
print soup.find_all(id="link2")
print soup.find_all(id=True)
print soup.find_all("a", class_="sister")
print soup.select("p.title")
print soup.find_all("a", attrs={"class": "sister"})
print soup.find_all(text="Elsie")
print soup.find_all(text=["Tillie", "Elsie", "Lacie"])
print soup.find_all("a", limit=2)

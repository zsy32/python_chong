
# -*-coding:utf-8-*-
import bs4
import requests
import scrapy
import html5lib
from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
"""

# soup = BeautifulSoup(html)

soup=BeautifulSoup(html, "lxml")

'''
print soup.prettify()
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
#  Elsie
# <class 'bs4.element.Comment'>


<p class="title" name="dromouse"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>


<p class="story">...</p>

for child in  soup.head.children:
    print child
if type(soup.a.string)==bs4.element.Comment:
    print soup.a.string
print soup.head.contents
#[<title>The Dormouse's story</title>]
print soup.head.contents[0]
#<title>The Dormouse's story</title>
print soup.head.children
#<listiterator object at 0x7f71457f5710>
for child in  soup.body.children:
    print child
print "abc"

<title>The Dormouse's story</title>
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print soup.title
#<title>The Dormouse's story</title>
print soup.a
#<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
print soup.p
#<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
print type(soup.a)
#<class 'bs4.element.Tag'>
print soup.name
print soup.head.name
#[document]
#head
print soup.p.attrs
#{'class': ['title'], 'name': 'dromouse'}
print soup.p['class']
#['title']
print soup.p.get('class')
#['title']print soup.attrs


soup.p['class']="newClass"
print soup.p
#<p class="newClass" name="drmouse"><b>The Dormouse's story</b></p>
del soup.p['class']
print soup.p
#<p name="dromouse"><b>The Dormouse's story</b></p>
print soup.p.string
#The Dormouse's story
print type(soup.p.string)
#<class 'bs4.element.NavigableString'>
print type(soup.name)
#<type 'unicode'>
print soup.name
# [document]
print soup.attrs
#{} 空字典
print "看"
print soup.a
print soup.a.string
print type(soup.a.string)
print soup.body.contents

print "2222"
print soup.body.contents[2]
'''
print "ss"

for child in soup.descendants:
    print child
    print "ss"
for child in soup.descendants:
    print child
print soup.head.string
#The Dormouse's story
print soup.title.string
#The Dormouse's story
print soup.html.string
# None
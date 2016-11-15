# -*-coding:utf-8-*-
from urllib2 import urlopen
import bs4
import requests
import scrapy
import html5lib
from bs4 import BeautifulSoup
import re


deskurl = "http://www.ftchinese.com/channel/chinareport"
html = urlopen(deskurl)
bsOBj = BeautifulSoup(html, "lxml", from_encoding="utf-8")
result_list = []
for link in bsOBj.find_all("a"):
    if 'href' in link.attrs:
        if 'story' in link.attrs['href']:
            text = unicode(link.string)
            result_list.append(text)
            print(text.encode("UTF-8"))
        # if link.attrs['class'][0] == 'nav-section-head':
        #     targetUrl = deskurl + link.attrs['href']
        #     print(targetUrl)
        # if link.attrs['class'] == "nav-section-head desktop":
        #     print(link.attrs['href'])



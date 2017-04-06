#!/usr/python3
import re
import urllib.request
def gethtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html
def getimg(html):
    reg = r'src="(.*?\.jpg)"'
    img=re.compile(reg)
    html=html.decode('utf-8')#python3
    imglist=re.findall(img,html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg'%x)
        x = x+1
html=gethtml("http://news.ifeng.com/a/20161115/50258273_0.shtml")

getimg(html)

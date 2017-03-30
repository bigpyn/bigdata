# -*- coding:utf-8 -*-
import urllib.request,re
#抓取捧腹网

#a = urllib.request.urlopen('http://www.baidu.com').read()
#a = urllib.request.urlopen('http://www.baidu.com').readline()
#print (a)

def page(pg):
    url = "http://www.pengfu.com/index_%s.html" % pg
    html = urllib.request.urlopen(url).read().decode('utf-8')
   # print(html)
    return html
#匹配标题
def Title(html):
    html = page(1)
    reg = re.compile(r'<h1 class="dp-b"><a href=".*?" target="_blank">(.*?)</a>')#编译，提高效率
    item = re.findall(reg,html)
   # print (item[0])
   # for r in item:
     #  print (r)
    return item
#匹配图片
def content(html):
    reg = r'<img src="(.*?)" width='
    item = re.findall(reg,html)
    #print(item)
    return item
#下载
def Down(url,name):
    path = 'img\%s.jpg'%name
    urllib.request.urlretrieve(url,path)

#多页，标题对应图片
for i in range(1,3):
    html = page(i)
    title_list = Title(html)
    content_title = content(html)
    for i,z in zip(title_list,content_title):
            #print(i, z)
            Down(z,i)
           # print(i,z)




#a = page(1)
#b = Title()
#c = content(html=)
#d = down(url,name)

# -*- coding:utf-8 -*-
import urllib#网页访问
import re
import MySQLdb

domain = 'http://www.ygdy8.net'

def getList(pn):
    html = urllib.urlopen('http://www.ygdy8.net/html/gndy/oumei/list_7_%s.html' %pn)#打开网站  对象
    text = html.read()#读出源代码
    text = text.decode('gb2312','ignore').encode('utf-8')#ignore忽略错误
    reg = re.compile(r'<a href="(.+?)" class="ulink">(.+?)</a>')#编译正则表达式   提升匹配效率
    return re.findall(reg,text)#正则匹配  1,url  2,名字

def getMvoie(url):
    html = urllib.urlopen(domain+url)
    text = html.read()
    text = text.decode('gb2312','ignore').encode('utf-8')
    reg = re.compile(r'<!--Content Start-->(.*?)</tbody>',re.S)#点号.除了换行符和制表符以外的其他字符   re.S:允许匹配多行
    return re.findall(reg,text)[0]

class Mysql(object):
    conn = MySQLdb.connect(
        host="mysql.litianqiang.com",
        port=7150,
        user="",
        passwd="",
        db="movie",
        charset="utf8",
    )
    def insert(self,title,content,movielink):
        cur = self.conn.cursor()
        cur.execute("insert into movie VALUES (NULL ,'%s' ,'%s' ,'%s')" %(title,content,movielink))
        cur.close()
        self.conn.commit()

mysql = Mysql()
n = 1
while True:
    if n > 155:break
    for i in getList(n):
        #i=('1.html','标题')
        url = i[0]
        title = i[1]
        content = getMvoie(url)
        movielink = re.findall(re.compile(r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)"'),content)[0]
        mysql.insert(title,content.replace("'",r"\'"),movielink)
        print ('插入数据 %s 完成' %title)
    n += 1

#-*- coding:utf-8 -*-
#获取源码
#从页面采集数据
#找到标题跟内容所对应的标签名
from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.pythontab.com/html/pythonhexinbiancheng/index.html'
url_list = [url] #链接放入列表，多页效果
for i in range(2,18):
	url_list.append('http://www.pythontab.com/html/pythonhexinbiancheng/%s.html' % i)
source_list = []#标题+文字
for j in url_list:
	request = urllib.request.urlopen(j)
	html = request.read()
	#print(html)
	soup = BeautifulSoup(html,'html.parser')#解析方式
	titles = soup.select('#catlist > li > a')#css选择器
	#print (titles)
	links = soup.select('#catlist > li > a')#吧标题跟所对应内容放在一起
	#print(links)
	for title,link in zip(titles,links):
		data = {
			"title" : title.get_text(),#获取标题文本
			"link" : link.get('href') #获取文章超链接
		}
		source_list.append(data)#把data数据直接追加到空列表
		#print(source_list) #标题+内容
		
		#获取文章内容
	for l in source_list:
		request = urllib.request.urlopen(l['link'])#找到链接，打开链接
		html = request.read()#读取源码
		soup = BeautifulSoup(html,'html.parser')
		text_p = soup .select('div.content > p')#查找到内容
		text = []
		#print(text_p) #内容
		for t in text_p:
			text.append(t.get_text().encode('utf-8'))#追加到空列表
		#print(text)
		#标题
		title_text = l['title'] #css选择器获取标题
		#title_text = title_text.replace('*','').replace('/','or').replace('"','')
		title_text = title_text.replace('*','').replace('/','or').replace('"',' ').replace('?','wenhao').replace(':',' ')
		print(title_text) 
		
		with open('study/%s.txt'%title_text,'wb') as f:
			for a in text:
				f.write(a)
		
		
	

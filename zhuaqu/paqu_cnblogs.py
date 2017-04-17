#!/usr/bin/python
#-*- coding:UTF-8 -*-
import urllib.request
import time
import bs4

class CnBlogsSpider:
	url = "https://ing.cnblogs.com/ajax/ing/GetIngList?IngListType=All&PageIndex=${pageNo}&PageSize=30&Tag=&_="
	
	#获取html
	def getHtml(self):
		request = urllib.request.Request(self.pageUrl)
		response = urllib.request.urlopen(request)
		self.html = response.read()
	
	#解析html
	def analyze(self):
		self.getHtml()
		bSoup = bs4.BeautifulSoup(self.html)
		divs = bSoup.find_all("div",class_='ing-item')
		for div in divs:
			img = div.find("img")['src']
			item = div.find("div",class_='feed_body')
			userName = item.find("a",class_="ing-author").text
			text = item.find("span",class_="ing_body").text
			pubtime = item.find("a",class_='ing_time').text
			star = item.find("img",class_='ing-icon') and True or False
			#print ('(头像:',img,'昵称:',userName,'闪存',text,'时间',pubtime,'星星',star,')')
			result = '(头像:',img,'昵称:',userName,'闪存',text,'时间',pubtime,'星星',star,')'
			#fo = open("foo.txt", "w+")
			#fo.write(img)
			with open('foo.txt','w') as fw:
				for k in userName:
				#print(k)
				fw.write(userName)
 
	
	def run(self,page):
		pageNo = 1
		while (pageNo <=page):
			self.pageUrl = self.url.replace('${pageNo}',str(pageNo))+str(int(time.time()))
			print ('-----------\r\n第',pageNo,'页的数据如下:',self.pageUrl)
			self.analyze()
			pageNo = pageNo +1
			
CnBlogsSpider().run(3)

#from Tkinter import *
from tkinter import *
#from ScrolledText import ScrolledText #文本滚动条
#import tkinter.scrolledtext
import tkinter.scrolledtext
import urllib,requests
import re  #正则表达式
import threading  #多线程处理与控制
import time
from bs4 import BeautifulSoup as bs

url_name = [] #放置url+name
a = 1 #页数
def get():
	global a
	hd = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
	url = 'http://www.budejie.com/video/' + str(a)
	html = requests.get(url,headers = hd).content.decode('utf-8')#发送get请求
	bs(html,'lxml')
	url_content = re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)',re.S)#编译,提高效率
	url_contents = re.findall(url_content,html)
	print(url_contents)
	for i in url_contents:
		url_reg = r'data-mp4="(.*?)">'
		url_items = re.finall(url_reg,i)
		#print(url_items)
		if url_items:#如有有视频存在，我就匹配名字，如果是图片或文字就不匹配
			name_reg = re.compile(r'<a href="/detail-.{8}?.html">(.*?)</a>')
			name_items = re.findall(name_reg,i)
			#print(name_items)
			for i,k in zip(name_items,url_items):
				url_name.append([i,k])	
				#print(i,k)
				
	return url_name	
id = 1#视频个数
def write():
	global id
	while id < 10:
		url_name = get()#调用获取视频及名字
		for i in url_name:#i[1]url  i[0]name
			urllib.urlretrieve(i[1],'vedio\\%s.mp4' % (i[0]).decode('utf-8').encode('gbk'))#下载方法
			text.insert(END,str(id)+'.'+i[1]+'\n'+i[0]+'\n')
			url_name.pop(0)
			id+=1
	var1.set('蘑菇头:视频连接和视频抓取完毕')

def start():
	th = threading.Thread(target=write)
	th.start()#运行
	
b = get()	
root = Tk()
root.title('大家很棒')
text = tkinter.scrolledtext.ScrolledText(root,font = ('微软雅黑',10))
text.grid()
button = Button(root,text = '开始爬去',font = ('微软雅黑',10),command = start)
button.grid()
var1 = StringVar()#通过tk方法绑定一个变量
label = Label(root,font = ('微软雅黑',10),fg = 'red',textvariable=var1)
label.grid()
var1.set('熊猫已准备')
root.mainloop()

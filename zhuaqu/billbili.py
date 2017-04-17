#-*-coding:utf-8-*-
import requests
import json
import time
import datetime

def datetime_to_time():
	current_mili_time = lambda:int(round(time.time() * 1000))
	return current_mili_time()
	


headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
	'Referer':'http://space.bilibili.com/2084361/',
	'Accept':'*/*',
	'Host':'space.bilibili.com',
	'Accept-Encoding':'gzip, deflate, sdch',
	'Accept-Language':'zh-CN,zh;q=0.8',
}

def getsource(url):
	mid = url.replace('http://space.bilibili.com/ajax/member/GetInfo?mid=','')
	playload = {
		#'_':datetime_to_timestamp_in_milliseconds(datetime.datetime.now()),
		'_':datetime.datetime.now(),
		'mid':mid,
	}
	print(playload)
	jsoncontent = requests.get('http://space.bilibili.com/ajax/member/GetInfo',headers,data=playload).content
	print(jsoncontent)
	jsDict = json.loads(jsoncontent)
	if jsDict['status'] =='True':
		try:
			jsData = jsDict.get('data')
			mid = jsData['mid']
			name = jsData['name']
			sex = jsData['sex']
			face = jsData['face']
			regtime = jsData['regtime']
			birthday = jsData['birthday']
			fans = jsData['fans']
		except Exception as e:
			print (u'字典匹配缺少数据',e)
		try:
			data = {
				u'用户id':mid,
				u'名字':name,
				u'性别':sex,
				u'头像url':face,
				u'注册时间':regtime,
				u'生日':birthday,
				u'fans':fans,
			}
			print(data)
		except Exception as e:
			print (u'数据插入失败',e)
urls = []
	
for i in range(1,250):
	url = 'http://space.bilibili.com/ajax/member/GetInfo?mid={}'.format(i)
	urls.append(url)

for i in urls:
	#print (datetime_to_time()())
	getsource(i)
	break

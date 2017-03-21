#coding:utf-8
#抓取赶集网信息
from bs4 import BeautifulSoup
#from urlparse import urljoin
#from urllib.parse import urlparse
from urllib.parse import urljoin
import requests
import csv
import html5lib

#想爬去一个网页，第一步干什么？

URL = 'http://bj.ganji.com/fang1/o%7Bpage%7Dp%7Bprice%7D/'
ADDR = 'http://bj.ganji.com'
start_page = 1
end_page = 10
price = 7
with open('info.csv','w+') as f:
	csv_writer = csv.writer(f,delimiter = ',')
	print ('start')
	while start_page < end_page:
		start_page += 1
		print('get:{0}'.format(URL.format(page=start_page,price=price)))
		response = requests.get(URL.format(page=start_page,price=price))
		html = BeautifulSoup(response.text,'html.parser')
		house_list = html.select('.f-list-item-wrap')
		#print (house_list)
		if not house_list:
			break
		for house in house_list:
			#house_title = house.select('.title > a')[0].string.encode('utf-8')
			#house_title = bytes(house.select('.title > a')[0].text,encoding = 'utf-8')
			house_title = house.select('.title > a')[0].text
			#house_title = bytes(house_title,encoding = 'utf-8')
			#print(type(house_title))
			house_addr = house.select('.address > .area > a')[-1].text
			#print(house_addr)
			#print(house.select('.price > .num'[0]))
			house_price = house.select('.price > .num')[0].text
			#house_price = house.select('.price > .num')[0].text
			house_URL = urljoin(ADDR,house.select('.title > a')[0]['href'])
			#house_URL = urljoin(ADDR,house.select('.title > a')[0]['href'])
			csv_writer.writerow([house_title,house_addr,house_price,house_URL])
print('end.....')
			
			
			
			

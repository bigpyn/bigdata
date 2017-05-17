import requests,threading
from lxml import etree
from bs4 import BeautifulSoup

def get_html(url):
	#url = 'https://www.doutula.com/article/list/?page=1'
	headers = {'User-Agent':'Mozilla'}
	request = requests.get(url = url,headers = headers)
	response = request.content
	return response

def get_img_html(html):
	soup = BeautifulSoup(html,'lxml')
	all_a = soup.find_all('a',class_='list-group-item')
	for i in all_a:
		img_html = get_html(i['href'])
		#print(img_html)
		get_img(img_html)

#图片url
def get_img(html):
	soup = etree.HTML(html)#初始化源码
	items = soup.xpath('//div[@class="artile_des"]')
	for item in items:
		imgurl_list = item.xpath('table/tbody/tr/td/a/img/@onerror')
		#print(imgurl_list)
		start_save_img(imgurl_list)
	
#下载图片
x = 1
def save_img(img_url):
	global x #全局变量
	x +=1
	img_url = img_url.split('=')[-1][1:-2].replace('jp','jpg')
	print(u'正在下载'+'http:'+img_url)
	img_content = requests.get('http:'+img_url).content
	with open('doutu/%s.jpg' % x,'wb') as f:
		f.write(img_content)
		
def start_save_img(imgurl_list):
	for i in imgurl_list:
		print(i)
		th = threading.Thread(target=save_img,args=(i,))
		th.start()

def main():
	start_url = 'https://www.doutula.com/article/list/?page='
	for i in range(1,10):
		start_html = get_html(start_url.format(i))
		get_img_html(start_html)
		
if __name__ =='__main__':
	main()	
		
#a = get_html(1)

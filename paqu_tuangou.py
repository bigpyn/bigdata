import urllib.request,urllib.error
#import csv
#爬出美团数据

def fetch(url):
	http_header = {'User-Agent':'Chrome'}
	http_request = urllib.request.Request(url,None,http_header)
	
	print ("start downloading data...")
	http_response = urllib.request.urlopen(http_request)
	print ("finish downloading data...")
	
	#status code
	#200
	print (http_response.code)
	print (http_response.info())
	
	print ('----data---')
	#with open('info.csv','w') as f:
	#csv_writer = csv.writer(f,delimiter = ',')
	print (http_response.read())
	#csv_writer.writerow(http_response.read())
	

if __name__ =="__main__":
	fetch("http://www.meituan.com/api/v1/divisions")

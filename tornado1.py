import tornado.curl_httpclient
#from tornado.httpclient import HTTPResponse, HTTPError, AsyncHTTPClient, main, _RequestProxy

def fetch(url):
	http_header={'User-Agent':'Chrome'}
	http_request=tornado.httpclient.HTTPRequest(url=url,method='GET',headers=http_header,connect_timeout=200, request_timeout=600)

	http_client=tornado.httpclient.HTTPClient()

	http_response=http_client.fetch(http_request)

	print (http_response.code)

	all_fields=http_response.headers.get_all()
	for field in all_fields:
		print (field)
	print (http_response.body)

if __name__=="__main__":
	fetch("http://www.baidu.com")

import tornado.httpclient
link='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
cli=tornado.httpclient.HTTPClient()
first=cli.fetch(link+"12345")
while True:
	data=first.body.decode('utf8')
	l=data.split(' ')
	new=link+l[-1]
	print(new)
	first=cli.fetch(new)

#http://www.cnblogs.com/itlqs/p/6055365.html
#测试urlparse
from urllib.parse import urlparse
o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
#>>> o   
#ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
#            params='', query='', fragment='')
# o.scheme
#'http'
# o.port
# o.geturl()
#'http://www.cwi.nl:80/%7Eguido/Python.html'

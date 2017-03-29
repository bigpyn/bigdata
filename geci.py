import urlparse

　　URLscheme = "http"

　　URLlocation = "www.python.org"

　　URLpath = "lib/module-urlparse.html"

　　modList = ("urllib", "urllib2", \

　　"httplib", "cgilib")

　　#将地址解析成组件

　　print "用Google搜索python时地址栏中URL的解析结果"

　　parsedTuple = urlparse.urlparse(

　　"http://www.google.com/search?

　　hl=en&q=python&btnG=Google+Search")

　　print parsedTuple

　　#将组件反解析成URL

　　print "\反解析python文档页面的URL"

　　unparsedURL = urlparse.urlunparse( \

　　(URLscheme, URLlocation, URLpath, '', '', ''))

　　print "\t" + unparsedURL

　　#将路径和新文件组成一个新的URL

　　print "\n利用拼接方式添加更多python文档页面的URL"

　　for mod in modList:

　　newURL = urlparse.urljoin(unparsedURL, \

　　"module-%s.html" % (mod))

　　print "\t" + newURL

　　#通过为路径添加一个子路径来组成一个新的URL

　　print "\n通过拼接子路径来生成Python文档页面的URL"

　　newURL = urlparse.urljoin(unparsedURL,

　　"module-urllib2/request-objects.html")

　　print "\t" + newURL

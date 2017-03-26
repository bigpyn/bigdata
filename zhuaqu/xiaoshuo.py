# coding:utf-8
import re
import urllib2


def Hello():
    url = "http://www.23us.com/"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read().decode('gbk', 'ignore')
    the_url = re.compile(
        '<li><p class="ul1">(.*?)<a class="poptext" href="(.*?)" target="_blank">(.*?)</a>.*?</p><p class="ul2"><a href=".*?" target="_blank">(.*?)</a></p><p>(.*?)</p>(.*?)</li>.*?',
        re.S)  # 正则匹配首页所有章节
    last_url = the_url.findall(content)

    for a, b, c, d, e, f in last_url:
        # print a
        pass
        the_url = re.compile('<li><p>.*?</p><a href="(.*?)" target="_blank">.*?</a></li>', re.S)  # 正则匹配最新小说木下之影
        last_url = the_url.findall(content)  # 对最新小说源码进行匹配筛选
        # print last_url
    for a in last_url:
        print a  # 打印a变量（其他类型）连接地址
        request = urllib2.Request(a)
        response = urllib2.urlopen(request)
        content = response.read().decode('gbk', 'ignore')
        the_url = re.compile('<td class="L"><a href="(.*?)">.*?</a></td>')  # 正则匹配最新小说里的所有章节
        last_url = the_url.findall(content)
        # print last_url  #打印出所有章节超链接
        for i in last_url:
            # print i  #循环打印出最新小说里每本小说的所有章节
            lasts_url = a + i
            # print lasts_url
            request = urllib2.Request(lasts_url)
            response = urllib2.urlopen(request)
            content = response.read()
            the_url = re.compile('content="text/html; charset=(.*?)"', re.S)
            last_code = the_url.findall(content)
            # print last_code
            for i in last_code:
                contents = content.decode(i)
                the_url = re.compile('.*?<title>(.*?)</title>.*?<dd id="contents">(.*?)</dd>.*?', re.S)
                lasts_content = the_url.findall(contents)
                # print lasts_content #打印最新小说里每本小说里所有章节的内容
            for i, j in lasts_content:  # 循环打印最新小说里每本小说里所有章节的内容
                f = open('yizhoukao.txt', 'a+')
                j = j.replace('&nbsp;', '').replace('<br /><br />', '\n')
                lasts_content = i + '\n\t' + j + '\n'
                f.write(lasts_content.encode('gbk'))
                f.close()


try:
    Hello()
except:
    try:
        Hello()
    except urllib2.URLError, e:
        f = open('error.txt', 'a+')
        f.write(str(e.reason))
        f.close()

此投票的爬虫代码中主要使用到requests、 bs4.BeautifulSoup、threading模块
#https://www.linuxyw.com/806.html

因为某件事，朋友们在网络上搞起投票行为，为了帮朋友们，特意用python写下了这个投票代码的爬虫

投票网站的某政府单位的网站，所以网站程序和代码大家应该懂的

网站投票没有对IP进行限制，也就是说，只要每刷新一次地址，就可以投票一次，但为了防止一个IP出现过多投票记录，所以在代码中，增加了代理IP的多个user-agent。

 

获取该网站的投票接口，用浏览器F12，就可以找到了


浏览器获取投票接口
 

代码如下：

1.#!/usr/bin/env python
2.# coding=utf-8
3.# 戴儒锋
4.# http://www.linuxyw.com
5.
6.
7.import re
8.import random
9.import sys
10.import time
11.import datetime
12.import threading
13.from random import choice
14.import requests
15.import bs4
16.
17.def get_ip():
18.    """获取代理IP"""
19.    url = "http://www.xicidaili.com/nn"
20.    headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
21.                "Accept-Encoding":"gzip, deflate, sdch",
22.                "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
23.                "Referer":"http://www.xicidaili.com",
24.                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
25.                }
26.
27.    r = requests.get(url,headers=headers)
28.    soup = bs4.BeautifulSoup(r.text, 'html.parser')
29.    data = soup.table.find_all("td")
30.
31.    ip_compile= re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')    # 匹配IP
32.    port_compile = re.compile(r'<td>(\d+)</td>')                # 匹配端口
33.    ip = re.findall(ip_compile,str(data))       # 获取所有IP
34.    port = re.findall(port_compile,str(data))   # 获取所有端口
35.
36.    return [":".join(i) for i in zip(ip,port)]  # 组合IP+端口，如：115.112.88.23:8080
37.
38.# 设置 user-agent列表，每次请求时，可在此列表中随机挑选一个user-agnet
39.uas = [
40.    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
41.    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
42.    "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
43.    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
44.    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
45.    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
46.    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
47.    ]
48.
49.def get_url(code=0,ips=[]):
50.    """
51.        投票
52.        如果因为代理IP不可用造成投票失败，则会自动换一个代理IP后继续投
53.    """
54.    try:
55.        ip = choice(ips)
56.    except:
57.        return False
58.    else:
59.        proxies = {
60.            "http":ip,
61.        }
62.
63.        headers2 = { "Accept":"text/html,application/xhtml+xml,application/xml;",
64.                        "Accept-Encoding":"gzip, deflate, sdch",
65.                        "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
66.                        "Referer":"",
67.                        "User-Agent":choice(uas),
68.                        }
69.    try:
70.        num = random.uniform(0,1)
71.        hz_url = "http://www.xxxxx.com/xxxx%s" % num   # 某投票网站的地址，这里不用真实的域名
72.        hz_r = requests.get(hz_url,headers=headers2,proxies=proxies)
73.    except requests.exceptions.ConnectionError:
74.        print "ConnectionError"
75.        if not ips:
76.            print "not ip"
77.            sys.exit()
78.
79.        # 删除不可用的代理IP
80.        if ip in ips:
81.            ips.remove(ip)
82.
83.        # 重新请求URL
84.        get_url(code,ips)
85.    else:
86.        date = datetime.datetime.now().strftime('%H:%M:%S')
87.        print u"第%s次 [%s] [%s]：投票%s (剩余可用代理IP数：%s)" % (code,date,ip,hz_r.text,len(ips))
88.
89.
90.ips = []
91.for i in xrange(6000):
92.    # 每隔1000次重新获取一次最新的代理IP，每次可获取最新的100个代理IP
93.    if i % 1000 == 0:
94.        ips.extend(get_ip())
95.    # 启用线程，隔1秒产生一个线程，可控制时间加快投票速度 ,time.sleep的最小单位是毫秒
96.    t1 = threading.Thread(target=get_url,args=(i,ips))
97.    t1.start()
98.    time.sleep(1)
 

投票效果：




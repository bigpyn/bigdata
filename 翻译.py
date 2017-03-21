#import urllib.request#请求
#response=urllib.request.urlopen("http://www.fishc.com")#响应
#html=response.read()
#html=html.unescapedecode("utf_8")
#print(html)
#import urllib.request
#import os
#os.chdir('C:\\Users\\Administrator\\Desktop\\py')
#response=urllib.request.urlopen("http://placekitten.com")
#cat_img=response.read()
#with open("cat_200_300.jpg",'wb')as f:
#    f.write(cat_img)
import urllib.request
import urllib.parse
import json
import time
#import random
import os
#url="http://www.whatismyip.com.tw"
#iplist=[ '122.96.59.99:80','175.17.227.36:8888','119.28.19.222:8888 ','182.203.4.176:8888','123.138.216.94:9999']
#proxy_support=urllib.request.ProxyHandler({"http":random.choice(iplist)})
#opener=urllib.request.build_opener(proxy_support)
#opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')]
#urllib.request.install_opener(opener)
#response=urllib.request.urlopen(url)
#html=response.read().decode("utf-8")
#print(html)

while True:
    contect=input("输入要翻译的内容：")
    if contect=="c":
       os.system("cls")
       continue
    url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    data={}
    data["type"]='AUTO'
    data["i"]=contect
    data["doctype"]="json"
    data["xmlVersion"]="1.8"
    data["keyfrom"]='fanyi.web'
    data["ue"]="UTF-8"
#data{"action"}='FY_BY_CLICKBUTTON'
    data["data"]="ture"
    data=urllib.parse.urlencode(data).encode("utf-8")
    req=urllib.request.Request(url,data)
    response=urllib.request.urlopen(url,data)
    req.add_header('User-Agent:','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko') 
    html=response.read().decode("utf-8")
    target=json.loads(html)
    print("翻译的结果是：%s"%(target["translateResult"][0][0]['tgt']))
    time.sleep(1)
    #if contect=="清除":
    #   os.system("cls")


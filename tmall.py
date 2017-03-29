#coding=utf-8
import requests;
from bs4 import BeautifulSoup;
import pymysql;
#定时器
import time;
from json import *;
import json

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='work',charset='utf8');
cursor = db.cursor();
cursor.execute("SET NAMES utf8");

headers = {
    'age':'1',
    'content-encoding':'gzip',
    'content-type':'text/html; charset=utf-8',
    'date':'Mon, 13 Feb 2017 06:21:25 GMT',
    'head-status':'M',
    'server':'JDWS/2.0',
    'status':'200',
    'ups':'f0-78|a35-140',
    'vary':'Accept-Encoding',
    'via':'BJ-H-NX-105(EXPIRED), http/1.1 SH-CT-1-JCS-112 ( [cMsSf ])',
}
jdUrl = 'https://list.jd.com'

jdIndexUrl = 'https://search.jd.com/'
#https://search.jd.com/Search?keyword=%E6%8A%A4%E7%90%86%E6%B6%B2%20%E9%9A%90%E5%BD%A2%E7%9C%BC%E9%95%9C&enc=utf-8&pvid=imkuu3zi.23k7jn
url = 'https://search.jd.com/search?keyword=%E6%8A%A4%E7%90%86%E6%B6%B2%20%E9%9A%90%E5%BD%A2%E7%9C%BC%E9%95%9C&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=2&cid2=12190&uc=0#J_searchWrap'
indexVal = requests.get(url,headers = headers)
indexVal.encoding = 'utf-8'
indexHtml = BeautifulSoup(indexVal.text,'html.parser')
clasText = indexHtml.select('.sl-v-list .v-fixed li a')
for clasUrl in clasText:
    urlEach = jdIndexUrl+clasUrl['href']
    #类名
    #print(clasUrl.text)
    thisIndex = requests.get(urlEach,headers = headers)
    thisIndex.encoding = 'utf-8'
    clasThisVal = BeautifulSoup(thisIndex.text,'html.parser')
    thisText = clasThisVal.select('#J_selector .s-category .sl-value .sl-v-list li a')
    # print(thisText)
    # continue
    for clas in thisText:
        #分类的连接
        #print(jdIndexUrl+clas['href'])
        url_th = requests.get(jdIndexUrl+clas['href'],headers = headers)
        url_th.encoding = 'utf-8'
        html_th = BeautifulSoup(url_th.text,'html.parser')
        #print(clas.text)
        if clas.text=='护理液':
            intUrl = 0
            while True:
                intVal = intUrl*2
                clasName = 'https://search.jd.com/s_new.php?keyword=护理液 隐形眼镜&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=2&wq=护理液 隐形眼镜&cid2=12190&cid3=12600&ev=exbrand_'+clasUrl.text+'%40&page='+str(intVal)+'&s=31&scrolling=y&pos=30&log_id=1487041071.61841&tpl=1_M&show_items=2280917,2302798,1845822,2302786,1090644580,2279932,1845886,3063602,1013413436,3260953,1033442236,10061304988,1014007863,1100384677,10694878534,1722982800,10128140400,1076216428,1125478497,1021968297,1360807623,10061304987,1121518342,1020401721,10842693732,10978845744,10513034392,1143631155,1170429133,10349569850'
                url_hl = requests.get(clasName,headers = headers)
                url_hl.encoding = 'utf-8'
                html_hl = BeautifulSoup(url_hl.text,'html.parser')
                #价钱
                money_hl = html_hl.select('.gl-item .p-price strong')
                #商品名
                commodity_hl = html_hl.select('.gl-item .p-name-type-2 em')
                #评价数
                evaluate_hl = html_hl.select('.gl-item .p-commit a')
                #print(evaluate_hl)
                #判断是否抓取到当前页
                if evaluate_hl==[]:
                    break
                #print(clasName)
                for each_li in range(len(evaluate_hl)):
                    #print(evaluate_hl[each_li].text)
                    #评价的转换
                    evaluate_hl_re = evaluate_hl[each_li].text.replace('+','')
                    if not(str(evaluate_hl_re.find('万'))==str(-1)):
                        evaluate_re = evaluate_hl_re.replace('万','')
                        evaluate_str = str(float(evaluate_re)*10000)
                        evaluate_hl_re = evaluate_str[:len(evaluate_str)-2]
                    #print(evaluate_hl_re)
                    if money_hl[each_li].text=='':
                        continue
                    try:
                        sql = "INSERT INTO JD(品牌,类型,商品名,金额,评价)VALUES('%s','%s','%s','%s','%s')" % (clasUrl.text,clas.text,commodity_hl[each_li].text,money_hl[each_li].text,evaluate_hl_re);
                        print(sql)
                        sql = sql.encode();
                        cursor.execute(sql);
                        db.commit();
                    except Exception as err:
                         db.commit();

                intUrl+=1
                #break
        #continue
        #如果不等于护理液产品就在当前页抓取
        if not(clas.text=='护理液'):
            #价钱
            yjHtml = html_th.select('.ml-wrap #J_goodsList ul .p-price i')
            #商品详细介绍
            yjClasVal = html_th.select('.ml-wrap #J_goodsList ul .p-name-type-2')
            #评论
            commentVal = html_th.select('.ml-wrap #J_goodsList ul .p-commit')
            #店铺名称
            shopVal = html_th.select('.p-shop')
            for each_html in range(len(yjHtml)):
                try:
                    sql = "INSERT INTO JD(品牌,类型,商品名,金额,评价)VALUES('%s','%s','%s','%s','%s')" % (clasUrl.text,clas.text,yjClasVal[each_html].text,yjHtml[each_html].text,commentVal[each_html].text);
                    print(sql)
                    sql = sql.encode();
                    cursor.execute(sql);
                    db.commit();
                except Exception as err:
                    db.commit();
        #break
    #break


db.close();

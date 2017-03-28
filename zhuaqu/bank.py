# -*- coding:utf-8 -*-
#1\爬虫
#2写入excel
#思路:爬虫：网页采集数据
#模块:urllib,re,requests,BeautifulSoup,urllib2
import urllib.request,re,xlwt#写excel，xlrd读取库

def getdata():
    url_list = []
    for i in range(1,20):
        url = 'http://furhr.com/?page={}'.format(i)
    try:
          a = urllib.request.urlopen(url).read() #打开地址
         # print(a)
    except Exception as e:
             print (e)
   # continue

#%s传字符串或者任何值
#format  {}  format
#创建excel表格，写入数据
#pip list查看模块
    w = re.compile(r' <tr><td>\d+</td><td>\d+</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>')#编译，提高效率
    page_list = re.findall(w,a)
    #print(page_list[0][0])
    url_list.append(page_list)
    return url_list

def excel_write(items):
    newTable = 'test123.xls' #表格名称
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('test1') #创建表
    headData = ['公司名称','电话','地址']
    for colnum in range(0,3):
        ws.write(0,colnum,headData[colnum],xlwt.easyxf('font:blod on'))#0行,colnum列,内容
    wb.save(newTable)
    print ('创建成功')

#写入数据
    index = 1 #代替的是数据
    for item in items:#银行信息
        for j in range(0,len(item)):
           # print(j)
            #print(item[j])
            for i in range(0,3):
               # print(item[j][i])
                ws.write(index,i,item[j][i])
            index +=1
        wb.save(newTable)
if __name__ =="__main__":
    items = getdata()
    excel_write(items)

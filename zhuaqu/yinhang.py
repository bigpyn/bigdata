# _*_coding:utf-8_*_
import urllib
import re
import urllib.request
import xlwt
def getdata():
    url_list=[]
    for i in range(1,20):
        url = 'http://furhr.com/?page={}'.format(i)
        try:
            html = urllib.request.urlopen(url).read().decode('utf-8')
        except Exception as e:
            print(e)
            continue
        #w = re.compile(r'<tr><td>(\d+)</td><td>(\d+)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>')
        page_list = re.findall(r'<tr><td>(\d+)</td><td>(\d+)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>',html)
        print(page_list)
        url_list.append(page_list)
    return  url_list
def write_excel(items):
    tablename = '1111.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('爬取数据')
    headtitle = ['序号','行号','网点名称','电话','地址']
    for column in range(0,5):
        ws.write(0,column,headtitle[column],xlwt.easyxf('font: bold on'))
    row = 1
    for item in items:
        for j in range(0,len(item)):
            for i in range(0,5):
                #print(item[0])
                ws.write(row,i,item[j][i])
            row +=1
        wb.save(tablename)
if __name__=='__main__':
    items = getdata()
    write_excel(items)

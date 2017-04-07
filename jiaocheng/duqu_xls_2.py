#-*- encoding: utf-8 -*-
# from html.parser import HTMLParser

# class MyParser(HTMLParser):
    # def __init__(self):
        # HTMLParser.__init__(self)        
        
    # def handle_starttag(self, tag, attrs):
        # # 这里重新定义了处理开始标签的函数
        # if tag == 'a':
            # # 判断标签<a>的属性
            # for name,value in attrs:
                # if name == 'href':
                    # print (value)
        

# if __name__ == '__main__':
    # a = '<html><head><title>test</title><body><a href="http://www.163.com">链接到163</a></body></html>'
    
    # my = MyParser()
    # # 传入要分析的数据，是html的。
    # my.feed(a)

# def power(x,y=2):
	# r = 1
	# for i in range(y):
		# r = r * x
	# return r
# print(power(3))
# print(power(3,3))
#! /usr/bin/env python
#coding=utf-8

# pyexcel_xls 以 OrderedDict 结构处理数据
# from collections import OrderedDict

# from pyexcel_xls import get_data
# from pyexcel_xls import save_data


# def read_xls_file():
    # xls_data = get_data(r"D:\read_test.xlsx")
    # print ("Get data type:", type(xls_data))
    # for sheet_n in xls_data.keys():
        # print (sheet_n, ":", xls_data[sheet_n])


# if __name__ == '__main__':
    # read_xls_file()
#! /usr/bin/env python
#coding=utf-8

# pyexcel_xls 以 OrderedDict 结构处理数据
from collections import OrderedDict

from pyexcel_xls import get_data
from pyexcel_xls import save_data


def read_xls_file():
    xls_data = get_data(unicode(r"D:\试试.xlsx", "utf-8"))
    print ("Get data type:", type(xls_data))
    for sheet_n in xls_data.keys():
        print (sheet_n, ":", xls_data[sheet_n])
    return xls_data


	
def save_xls_file():
    data = OrderedDict()
    # sheet表的数据
    sheet_1 = []
    row_1_data = [u"ID", u"昵称", u"等级"]   # 每一行的数据
    row_2_data = [4, 5, 6]
    # 逐条添加数据
    sheet_1.append(row_1_data)
    sheet_1.append(row_2_data)
    # 添加sheet表
    data.update({u"这是XX表": sheet_1})

    # 保存成xls文件
    save_data("D:\write_test.xls", data)


if __name__ == '__main__':
    save_xls_file()






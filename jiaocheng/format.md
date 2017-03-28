
#b、d\o\x分别表示二进制、十进制、八进制和十六进制
num = 25
print('{:b}'.format(num))
print('{:d}'.format(num))
print('{:o}'.format(num))
print('{:x}'.format(num))

#2精度与类型f
num = 123.23423
print('{:.2f}'.format(num))
#其中.2表示长度为2的精度，f表示float类型

#格式限定符
#语法是{:}
#1填充与对齐
#^\<\>分别是剧中、左对齐、右对齐，后面带宽度.:后面带填充的字符，只能是一个字符，不指定默认用户空格填充
num = 234
print('{:>8}'.format(num))
print('{:*>8}'.format(num))
#下标获取元素
info = ['bigberg',18]
msg = '{0[0]},{0[1]}'.format(info)
print(msg)

#语法
#通过{}和:来代替 %
#事件
name = "bigberg"
age = 18
msg1 = "my name is {},and my age is {}.".format(name,age)
msg2 = "my name is {0},and my age is {1}".format(name,age)
msg3 = "my name is {_name}, and my age is {_age}".format(_name=name,_age=age)
msg4 = "my name is {1},and my age is {0},and my brother's age is {0}".format(age,name)
print(msg1)
print(msg2)
print(msg3)
print(msg4)

#open()打开文件
#f = open("yesterday","r",encoding="utf-8")
#读取数据
#data = f.read()
#打印读取的文件
#print(data)
#关闭文件
#f.close()
#打开文件的模式有:
#r,只读模式（默认）
#w,只写模式。[不可读；不存在则创建；存在则删除内容;]
#a,追加模式，【可读；不存在则创建；存在则只追加内容；】
#"+"表示可以同时读写某文件
#r+,可读写文件[可读；可写；可追加]
#w+,写读
#a+同a
#"U"表示在读取时，可以将\r\n\r\n自动转换陈\n(与r或r+模式同使用)
#rU
#r+U
#"b"表示处理二进制文件(如:ftp发送上传ISO景象文件，linux可忽略,windows处理二进制文件时)
#rb
#wb
#ab
#with语句打开文件
#使用with语句打开文件，不需要在最后使用f.close()来关闭文件，with执行完毕之后会自动关闭

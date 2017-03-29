# -*- coding:utf-8 -*-
from tkinter import *

app = Tk()
app.title('数字进制转换')

def td():
    def nzs(num, jz):
        return (int(str(num), int(jz)))
    def test(nr):
        return nr.isdigit()
    def sd():
        p.set(nzs(e3.get(), e4.get()))
        print('转换结果 = ' + str(p.get()))
    ntd = Tk()
    ntd.title('2-36进制转换十进制通道:')
    testCMD = ntd.register(test)
    e4 = Entry(ntd, validate='key', validatecommand=(testCMD, '%P'),\
           invalidcommand=testt)
    e4.grid(row=0, column=0)
    Label(ntd, text='进制转换为十进制：').grid(row=0, column=1)
    Label(ntd, text='待转换数:').grid(row=1, column=0)
    e3 = Entry(ntd, validate='key', validatecommand=(testCMD, '%P'),\
           invalidcommand=testt)
    e3.grid(row=1, column=1)
    Label(ntd, text='转换结果:').grid(row=2, column=0)
    p = StringVar()
    e5 = Entry(ntd, state='readonly', textvariable=p)
    e5.grid(row=2, column=1)
    Button(ntd, text='开始转换', command=sd).grid(row=3, column=1)


def testt():
    e1.delete(0, END)
    return True

def test(nr):
    return nr.isdigit()

def new():
    root = Tk()
    root.title('关于作者:')
    Label(root, text='''关于本程序：

本程序提供了二进制、八进制、十进制、十六进制的互相转换。
到目前为止因本人技术原因还只能支持整数，请谅解，欢迎各位来QQ提出您的建议。

制作者：墉中孤影（笔名）       QQ：3331432116''').pack()

def neww():
    mm = Tk()
    mm.title('关于进制：')
    Label(mm, text='''进制
    进制也就是进位制，是人们利用符号进行计数的科学方法。
    对于任何一种进制---X进制，就表示某一位置上的数运算时是逢X进一位。
    十进制是逢十进一，十六进制是逢十六进一，二进制就是逢二进一。
    数制也称计数制，是指用一组固定的符号和统一的规则来表示数值的方法。
    计算机是信息处理的工具，任何信息必须转换成二进制形式数据后才能由计算机进行处理，存储和传输。
    人们通常使用的是十进制。它的特点有两个：有0，1，2…，9十个基本数字组成，十进制数运算是按“逢十进一”的规则进行的。
    在计算机中，除了十进制数外，经常使用的数制还有二进制数和十六进制数。
    在运算中它们分别遵循的是逢二进一和逢十六进一的法则。''').pack()

def po():
    e2.delete(0, END)
    num = e1.get()
    v1 = v.get()
    b1 = b.get()
    if v1==b1:
        n.set(num)
    if v1==1:
        if b1==2:
            n.set(zh.ezb(num))
        elif b1==3:
            n.set(zh.ezs(num))
        elif b1==4:
            n.set(zh.ezsl(num))
    elif v1==2:
        if b1==1:
            n.set(zh.bze(num))
        elif b1==3:
            n.set(zh.bzs(num))
        elif b1==4:
            n.set(zh.bzsl(num))
    elif v1==3:
        if b1==1:
            n.set(zh.sze(num))
        elif b1==2:
            n.set(zh.szb(num))
        elif b1==4:
            n.set(zh.szsl(num))
    elif v1==4:
        if b1==1:
            n.set(zh.slze(num))
        elif b1==2:
            n.set(zh.slzb(num))
        elif b1==3:
            n.set(zh.slzs(num))

    # 清空   e1.delete(0, END)

class Zh:
    def sze(self, num):
        return (bin(int(num))[2:])
    def ezs(self, num):
        return (int(str(num), 2))
    def szb(self, num):
        return (oct(int(num))[2:])
    def bzs(self, num):
        return (int(str(num), 8))
    def szsl(self, num):
        return (hex(int(num))[2:])
    def slzs(self, num):
         return (int(str(num), 16))
    def ezb(self, num):
        return (oct(int(str(num), 2))[2:])
    def bze(self, num):
        return (bin(int(str(num), 8))[2:])
    def ezsl(self, num):
        return (hex(int(str(num), 2))[2:])
    def slze(self, num):
        return (bin(int(str(num), 16))[2:])
    def bzsl(self, num):
        return (hex(int(str(num), 8))[2:])
    def slzb(self, num):
        return (oct(int(str(num), 16))[2:])

zh = Zh()

v = IntVar()
Radiobutton(app, text='二进制', variable=v, value=1).grid(row=0, column=0)
Radiobutton(app, text='八进制', variable=v, value=2).grid(row=0, column=1)
Radiobutton(app, text='十进制', variable=v, value=3).grid(row=0, column=2)
Radiobutton(app, text='十六进制', variable=v, value=4).grid(row=0, column=3)

testCMD = app.register(test)
Label(app, text='待转换数：').grid(row=1, column=1)
e1 = Entry(app, validate='key', validatecommand=(testCMD, '%P'),\
           invalidcommand=testt)
e1.grid(row=1, column=2)

b = IntVar()
Radiobutton(app, text='二进制', variable=b, value=1).grid(row=2, column=0)
Radiobutton(app, text='八进制', variable=b, value=2).grid(row=2, column=1)
Radiobutton(app, text='十进制', variable=b, value=3).grid(row=2, column=2)
Radiobutton(app, text='十六进制', variable=b, value=4).grid(row=2, column=3)

n = StringVar()
Label(app, text='转换结果：').grid(row=3, column=1)
e2 = Entry(app, state='readonly', textvariable=n)
e2.grid(row=3, column=2)

b1 = Button(app, text='开始转换', command=po)
b1.grid(row=4, column=2)

Button(app, text='退出程序', command=app.quit).grid(row=4, column=3)
Button(app, text='关于作者', command=new).grid(row=4, column=0)
Button(app, text='关于进制', command=neww).grid(row=4, column=1)

mainloop()

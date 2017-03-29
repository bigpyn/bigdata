#!/usr/bin/env python
# coding:utf-8
import threading
from time import ctime,sleep
def f1():
    for i in range(4):
        print (u'看书...',ctime())
        sleep(1)
    #lock.release()
def f2():
    for i in range(2):
        print (u'听音乐...',ctime())
        sleep(1)
threads = []
t1=threading.Thread(target=f1)
threads.append(t1)
t2=threading.Thread(target=f2)
threads.append(t2)        

if __name__=='__main__':
    print (u'开始时间',ctime())
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
print (u'结束',ctime())

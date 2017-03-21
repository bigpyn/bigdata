#!/usr/bin/python3

import queue
import threading
import time

exitFlag = 0 #进入标记赋值0

class myThread (threading.Thread): #类 我的线程（线程正进行，线程）
    def __init__(self, threadID, name, q):#构造函数（自己，线程ID，名字，q）
        threading.Thread.__init__(self)#调用父类构造函数
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):#跑函数
        print ("开启线程：" + self.name+"\n")#开启线程：名字
        process_data(self.name, self.q)#处理数据（名字，q）
        print ("退出线程：" + self.name+"\n")#退出线程：名字

def process_data(threadName, q):#处理数据（线程名，q）
    while not exitFlag:#当进入标记取不为真时
        queueLock.acquire()#队列锁，获得
        if not workQueue.empty():#如果工作的队列不为空时
            data = q.get()#获取队列赋值给数据
        
            queueLock.release()#队列锁释放
            print ("%s processing %s\n" % (threadName, data))#线程处理数据
        else:#另外
            queueLock.release()#队列锁释放
        time.sleep(2)#睡眠1s

threadList = ["Thread-1", "Thread-2", "Thread-3"]#线程列表
nameList = ["One", "Two", "Three", "Four", "Five"]#名字列表
queueLock = threading.Lock()#队列锁函数赋值队列锁
workQueue = queue.Queue(10)#队列对象长度10赋值给工作队列
threads = []#建立空列表赋值给threads
threadID = 1#线程ID

# 创建新线程
for tName in threadList:#名字在队列中循环
    thread = myThread(threadID, tName, workQueue)#我的线程（线程ID，名字，工作线程）赋值给线程
    thread.start()#线程开始
    threads.append(thread)#线程增加入threads
    threadID += 1#线程ID加1
# 填充队列
queueLock.acquire()#线程锁，获得
for word in nameList:#word在名字列表中循环
    workQueue.put(word)#工作队列写入队列名字
queueLock.release()#队列锁，释放


# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
    

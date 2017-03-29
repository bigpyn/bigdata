
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# task.py

import random, time, Queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	pass
	
QueueManager.register('get_task_queue')

server_addr = '10.135.90.95'
print('Connect to server %s ...' % server_addr)

m = QueueManager(address=(server_addr, 50000), authkey='abc')
m.connect()

# 获得通过网络访问的Queue对象
task = m.get_task_queue()
# 加入任务
task.put('hello')

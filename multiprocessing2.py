# -*- coding: utf-8 -*-

from multiprocessing.dummy import Pool as ThreadPool
import time


def fun(msg):
    print('msg: ', msg)
    time.sleep(1)
    return 'fun_return %s' % msg

pool = ThreadPool(processes=4)
results =[]
for i in range(5):
    msg = 'msg: %d' % i
    result = pool.apply(fun, (msg, ))
    results.append(result)

print(results)

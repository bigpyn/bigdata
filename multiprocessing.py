# -*- coding: utf-8 -*-

from multiprocessing.dummy import Pool as ThreadPool
import time


def fun(msg):
    print('msg: ', msg)
    time.sleep(1)
    return 'fun_return %s' % msg

arg = [3, 5, 11, 19, 12]
pool = ThreadPool(processes=3)
return_list = pool.map(fun, arg)
pool.close()
pool.join()
print(return_list)

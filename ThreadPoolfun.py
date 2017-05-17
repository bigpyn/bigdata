from multiprocessing.dummy import Pool#一共有四种获取线程函数返回值得方法，map、map_async、apply、apply_async：
# -*- coding: utf-8 -*-

from multiprocessing.dummy import Pool as ThreadPool
import time


def fun(msg):
    print('msg: ', msg)
    time.sleep(1)
    print('********')
    return 'fun_return %s' % msg


# map_async
print('\n------map_async-------')
arg = [1, 2, 10, 11, 18]
async_pool = ThreadPool(processes=4)
result = async_pool.map_async(fun, arg)
print(result.ready())  # 线程函数是否已经启动了
print('map_async: 不堵塞')
result.wait()  # 等待所有线程函数执行完毕
print('after wait')
if result.ready():  # 线程函数是否已经启动了
    if result.successful():  # 线程函数是否执行成功
        print(result.get())  # 线程函数返回值

# map
print('\n------map-------')
arg = [3, 5, 11, 19, 12]
pool = ThreadPool(processes=3)
return_list = pool.map(fun, arg)
print('map: 堵塞')
pool.close()
pool.join()
print(return_list)

# apply_async
print('\n------apply_async-------')
async_pool = ThreadPool(processes=4)
results =[]
for i in range(5):
    msg = 'msg: %d' % i
    result = async_pool.apply_async(fun, (msg, ))
    results.append(result)

for i in results:
    if i.ready():  # 线程函数是否已经启动了
        if i.successful():  # 线程函数是否执行成功
            print(i.get())  # 线程函数返回值


print('apply_async: 不堵塞')
# async_pool.close()
# async_pool.join()
for i in results:
    i.wait()  # 等待线程函数执行完毕

for i in results:
    if i.ready():  # 线程函数是否已经启动了
        if i.successful():  # 线程函数是否执行成功
            print(i.get())  # 线程函数返回值

# apply
print('\n------apply-------')
pool = ThreadPool(processes=4)
results =[]
for i in range(5):
    msg = 'msg: %d' % i
    result = pool.apply(fun, (msg, ))
    results.append(result)

print('apply: 堵塞')
print(results)

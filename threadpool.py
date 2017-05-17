# -*- coding: utf-8 -*-
import threadpool


def hello(a):
    return 'hello: %s' % a

hello_results = []

def print_result(req, result):
    hello_results.append(result)
    print('The result is %s %s' % (req.requestID, result))

data1 = [1, 2, 3, 4, 5]
requests = threadpool.makeRequests(hello, data1, print_result)
pool = threadpool.ThreadPool(5)
[pool.putRequest(req) for req in requests]

pool.wait()
print(hello_results)

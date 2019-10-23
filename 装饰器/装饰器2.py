#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
# 装饰器自身为函数，被装饰的对象为函数，且带参数
from functools import wraps
import time

def timeit(cpu_time=False):
    time_func = time.clock() if cpu_time else time.time
    def dec(fn):
        @wraps(fn)
        def wrap(*args, **kwargs):
            start = time_func()
            ret = fn(*args, **kwargs)
            print(time_func() - start)
            return ret
        return wrap
    return dec

@timeit(False)
def sleep(n):
    time.sleep(n)
    return n

sleep(1)
print(sleep.__name__)

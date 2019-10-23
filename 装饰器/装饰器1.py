#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei

"""装饰器为函数"""
# 被装饰对象为函数且不带参数

from time import sleep as sleeping
from time import time as nowTime
from functools import wraps

def timeit(fn):
    @wraps(fn)
    def wrap(*args, **kwargs):
        start = nowTime()
        ret = fn(*args, **kwargs)
        print(nowTime() - start)
        return ret
    return wrap
@timeit
def sleep(n):
    sleeping(n)
    print("我睡了%d秒" % n)
    return n
# 调用装饰后的sleep函数
sleep(1)
print(sleep.__name__)






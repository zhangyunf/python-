#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import time

def run_time(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('%s运行了%s' % (func.__name__, end_time - start_time))
        return result
    return wrapper






#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
# 装饰器自身为函数，被修饰对象为类，且不带参数
from functools import wraps

def singleton(cls):
    # 在装饰器中声明一个变量，用来保存类的示例，那么这个实例对象将始终是通一个实例对象
    instance = None
    @wraps(cls)
    def wrap(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance
    return wrap

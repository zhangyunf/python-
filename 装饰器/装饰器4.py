#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
from functools import wraps

def singleton(instance = False):
    name = 'yhy did it' if instance else 'yhy didn\'t it'
    def dec(cls):
        instance = None
        @wraps(cls)
        def wrap(*args, **kwargs):
            nonlocal instance
            print(name)
            if instance is None:
                instance = cls(*args, **kwargs)
            return instance
        return wrap
    return dec

@singleton(True)
class A:
    def __init__(self):
        self.name = 'yhy'

a = A()
print(id(a))
b = A()
print(id(b))


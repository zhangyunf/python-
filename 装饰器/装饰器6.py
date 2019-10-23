#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
from functools import wraps, partial

# 装饰器自身为类
class staticmethod:

    def __init__(self, method):
        wraps(method)(self)

    def __get__(self, instance, owner):
        # 通过partial函数返回一个带有None参数的add函数，因此在调用a.add()就不用传递参数了
        return partial(self.__wrapped__)

class Add:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    @staticmethod
    def add():
        print('I am static method')


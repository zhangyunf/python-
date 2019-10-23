#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
from functools import wraps

class TypeCheck:
    def __init__(self, srcType, dstType):
        self.srcType = srcType
        self.dstType = dstType

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.srcType]

    def __set__(self, instance, value):
        if isinstance(value, self.dstType):
            instance.__dict__[self.srcType] = value
        else:
            raise TypeError('{} should be {}'.format(value, self.dstType))
# 装饰器自身是一个函数
def typeassert(**kwargs):
    def dec(cls):
        def wraps(*args):
            for name, required_type in kwargs.items():
                setattr(cls, name, TypeCheck(name, required_type))
                return cls(*args)
        return wraps
    return dec
# 装饰对象是一个类，且带参数
@typeassert(name=str, age=int)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 实例化新的Person类，这里相当于调用的是wraps函数
p = Person('yhy', 18)
print(p.name)
print(p.age)
# 装饰器修改后的Person类为下面这个新的Person类，因此实例化Person的时候，调用的是下面这个新的Person类
class Person:
    name = TypeCheck('name', str)
    age = TypeCheck('age', str)

    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age


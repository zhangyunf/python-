#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei

'''
shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式
'''
import shelve

name = ["name1", "name2", "name3"]

class MyClass(object):

    def __init__(self):
        print("hello")

with shelve.open("b") as file:
    # 持久化列表
    file["test"] = name
    # 持久化类
    file["MyClass"] = MyClass()
    name1 = file["test"]
    print(type(name1))
    myclass = file["MyClass"]
    print(myclass)

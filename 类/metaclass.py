#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
'''
__new__
__metaclass__:
'''

class MyType(type):
    def __init__(self, what, bases=None, dict=None):
        print("--MyType init--")
        super(MyType, self).__new__(what, bases, dict)

    def __call__(self, *args, **kwargs):
        print("--MyType call--")
        obj = self.__new__(self, *args, **kwargs)#Foo的new
        obj.data = {"name": "zhangsan"}
        self.__init__(obj, *args, **kwargs)#init

class Foo(object):
    __metaclass__ = MyType#定义Foo类如何被定义
    def __init__(self, name):
        self.name = name
        print("Foo --init--")
    def __new__(cls, *args, **kwargs):
        print("Foo --new--")
        return object.__new__(cls)#继承父类的new方法，这里的cls相当于self/Foo
f = Foo("张三")


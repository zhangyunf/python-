#-*- coding:utf-8 -*-
#!Author:YunFei Zhang

class Dog(object):
    def __init__(self, name):
        self.name = name
    @staticmethod #实际上跟类没什么关系
    def eat(obj, food):
        print("%s is eating %s" % (obj.name, food))
d = Dog("zhangsan")
d.eat(d, "包子")
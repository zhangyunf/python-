#-*- coding:utf-8 -*-
#!Author:YunFei Zhang

class Dog(object):
    n = 333
    def __init__(self, name):
        self.name = name
    @classmethod
    def eat(cls, food):
        print("%s is eating %s" % (cls.n, food))#无法访问实例变量self.name,但是如果变成类变量n的话就可以了。
    def talk(self):
        print()
d = Dog("zhangsan")
d.eat("包子")
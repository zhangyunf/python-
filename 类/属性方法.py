#-*- coding:utf-8 -*-
#!Author:YunFei Zhang

class Dog(object):
    def __init__(self, name):
        self.name = name
        self.__food = None

    @property #将一个方法变成一个静态属性，所以要调用的话不能加()了
    def eat(self):
        print("%s is eating %s" % (self.name, self.__food))
    #给用属性方法修饰的函数赋值
    @eat.setter
    def eat(self, food):
        print("%s is eating %s" % (self.name, food))
        self.__food = food
    #删除
    @eat.deleter
    def eat(self):
        del self.__food
        print("删完了")
d = Dog("zhangsan")
#调用但是不能加()了
d.eat
#赋值,先存一个私有属性，然后修改的时候讲私有属性修改了。
d.eat = ("包子")
d.eat
#删除
del d.eat




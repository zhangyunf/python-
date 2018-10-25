#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
class Dog(object):
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("%s is eating...," % self.name)

def talk(self):
    print("%s is yelling..." % self.name)
d = Dog("张三")
#当用户输入eat时调用eat函数
choice = input(">>:").strip()
if hasattr(d, choice):#判断一个对象里是否有对应的字符串的方法
    func = getattr(d, choice)#获取方法
    func()
else:
    #添加方法
    '''
    setattr(d, choice, talk)
    d.talk(d)
    '''
    #添加属性
    setattr(d, choice, 22)
    print(getattr(d, choice))
#删除属性
delattr(d, "name")
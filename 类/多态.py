#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
'''
多态：一个接口，多种实现。实现接口的重用。
作用：就是为了在继承和派生的时候，保证使用“家谱”中任一类的实例的某一种属性时的正确调用。
'''

class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass #raise NotImplementedError("Subclass must implement abstract metho")
    @staticmethod
    def animal(obj):
        obj.talk()

class Cat(Animal):
    def talk(self):
        print("Meow")
class Dog(Animal):
    def talk(self):
        print("Woof Woof")
cat = Cat("张三")
dog = Dog("李四")

'''
调用一个接口，实现所有的动物的叫。接口重用。
在Animal中添加animal函数实现talk的调用。
'''


Animal(cat)
Animal(dog)

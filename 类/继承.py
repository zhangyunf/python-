#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
'''
注释：多继承时，继承优先有构造函数的构造函数。
'''

class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print("%s is eating.." % self.name)
    def sleep(self):
        print("%s is sleeping.." % self.name)
class Relation(object):
    def make_friends(self, obj):
        print("%s make friends %s" % (self.name, obj.name))

class Man(People, Relation):#继承People
    #重构初始化
    def __init__(self, name, age, money):
        #People.__init__(self, name, age)
        super(Man, self).__init__(name, age)
        self.money = money

    #重写父类方法
    def sleep(self):
        People.sleep(self)
        print("sleeping...")
class Women(People, Relation):#多继承,从左到右,先继承了People，所以在Relation中可以使用name的属性
    def brith(self):
        print("brith...")


m1 = Man("张三", 15, 155)
m2 = Women("lisi", 16)
m1.make_friends(m2)
m1.eat()
#B-->C-->A python3 广度优先
#B-->A-->C python2 深度优先
'''
python2 经典类是按深度优先来继承的，新式类是按广度优先继承的
python3 全是广度优先
'''
class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
class C(A):
    def __init__(self):
        print("C")
class D(B, C):
    pass
d = D()

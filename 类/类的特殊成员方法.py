#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
class Dog(object):
    '''描述类的信息'''
    def __init__(self, name):
        self.name = name
    @staticmethod #实际上跟类没什么关系
    def eat(obj, food):
        print("%s is eating %s" % (obj.name, food))
    def __call__(self, *args, **kwargs):
        print(*args, **kwargs)
    def __str__(self):
        return "my name is " + self.name

print(Dog.__doc__)#类的描述信息
d = Dog("zhangsan")
d("fda")#__call__方法调用
#查看类或对象的所有成员,通过类调用，打印类里所有的属性，不包括实例属性
print(Dog.__dict__)
#打印所有的实例属性，不包括类属性。
print(d.__dict__)
print(d)#添加__str__方法后，默认打印返回值
from lib.aa import C
c = C()
print(c.__module__)#打印模块lib.aa
print(c.__class__)#打印lib.aa.C
#将字典封装成一个类，可以控制权限
class Foo(object):
    def __init__(self):
        self.data = {}
    def __getitem__(self, item):
        print("__getitem__", item)
        return self.data.get(item)
    def __setitem__(self, key, value):
        print("__setitem__", key, value)
        self.data[key] = value
    def __delitem__(self, key):
        print("__delitem", key)
f = Foo()
f["name"] = "zhangsan"
print(f.data)
del f["name"]
'''
__new__

'''
class Fo(object):
    def __int__(self, name):
        self.name = name

f1 = Fo()
print(type(f1))#<class '__main__.Fo'>, f1类来自FO
print(type(Fo))#<class 'type'>, Fo类来自type
'''
将func、talk、__init__的类加载到Test的类里。
type("Test", (object), {"func":func})中，Test是类名， object是继承的类， 字典里是存在的函数
'''
def func(self):
    print("外部函数")
def talk(self):
    print("%s talk" % self.name)
def __init__(self, name, age):
    self.name = name
    self.age = age
Test = type("Test", (object,), {"func": func,
                               "talk": talk,
                               "__init__":__init__})
t = Test("张三", 22)
t.func()
t.talk()
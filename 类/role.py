#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
from selenium import webdriver

brower = webdriver.Ie()
'''
析构函数：在实例释放、销毁的时候执行的，通常用于做一些收尾工作，如关闭一些数据库连接，
          打开临时文件
私有方法、私有属性：
'''

class Role:
    '''
    类变量,可以使用类名直接调用，也可以用实例对象调用。
    但是如果和实例变量同名的话，会先找实例本身，如果没有再去类里面找。
    作用：大家共用的属性，节省开销。
    '''
    n = 123
    lis = []
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        #构造函数
        #在实例化时做一些类的初始化工作
        self.name = name#实例变量(静态属性)，作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value#私有属性
    def __del__(self):
        #析构函数
        print("彻底死了")

    def __show_status(self):#私有方法
        print("私有方法")
    def shot(self):#类的方法，功能（动态属性）
        print("shooting...")
r1 = Role("zhangsan", "police", "AK47")
#添加属性，只是给当前实例增加属性值，别的实例是没有的，
r1.bullet_prove = True
#删除属性，只是给当前实例增加属性值，别的实例是没有的，
del r1.bullet_prove
#使用实例修改类变量，相当于给r1增加了一个实例变量n并赋值为456
r1.n = 456

#使用类名
Role.n = 789
#修改
r1.lis.append("q")
#删除r1实例
#del r1
r2 = Role("lisi", "police", "AK47")
print(r2.n, r2.lis, Role.lis)

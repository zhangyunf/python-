#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
'''
装饰器：本质上是函数（装饰其他函数），就是为其他函数添加附加功能。
原则：1、不能修改被装饰的函数的源代码
      2、不能修改被装饰的函数的调用方式
实现装饰器知识储备：1.函数即“变量”
                    2.高阶函数（a.把一个函数名当做实参传给另外一个函数(不修改被装饰函数源代码的情况下为其添加功能)；
                                b.返回值中包含函数名（不修改函数的调用方法））
                    3.嵌套函数
高阶函数 + 嵌套函数 =》 装饰器
'''
#高阶函数
import time
'''
源代码
'''
'''
def func():
    time.sleep(3)
    print("in the func")
'''
'''
改变了源代码的调用方式，但是实现了不修改源代码的基础上增加了功能
'''
'''
def test1(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print("the func run time is %s" % (stop_time - start_time))
test1(func)
'''
'''
使原函数的调用方法不变
'''
'''
def test2(func):
    print(func)
    return func

print(test2(func))
func = test2(func)
func()#run func
'''
#嵌套函数:在一个函数的函数体内声明一个函数
'''
def foo():
    print("in the foo")
    def func():
        time.sleep(3)
        print("in the func")
    start_time = time.time()
    func()
    stop_time = time.time()
    print("the run time is %s" % (stop_time - start_time))
foo()
'''
#装饰器：给test3的函数增加一个统计运行时间的功能
'''
def test5(func):
    def test4():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the run time is %s" % (stop_time - start_time))
    return test4
'''
'''
def test5(func):
    def test4(*ars, **kwargs):
        start_time = time.time()
        func(*ars, **kwargs)
        stop_time = time.time()
        print("the run time is %s" % (stop_time - start_time))
    return test4
@test5#添加装饰的函数相当于在调用test3时，先执行了 test3 = test5(test3),将test5的返回值（test4的指针）。如所以此时执行test3时实际上是在执行test4。
def test3():
    time.sleep(3)
    print("in the test3")

test3()
'''
#高级版
'''
需求：模拟
'''
user, passwd = "zhangsan", "abc123"

def auth(auth_type):
    print(auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print("wrapper")
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password:").strip()
                if user == username and passwd == password:
                    print("开始登录")
                    return func(*args, **kwargs)
                else:
                    print("登录失败！")
            elif auth_type == "ldap":
                print("ldap")
                func(*args, **kwargs)
        return wrapper
    return outer_wrapper


def index():
    print("welcome to index page")
@auth(auth_type="local")#home=wrapper()
def login(*args, **kwargs):
    print("welcome to login page")
    return "from home"
@auth(auth_type="ldap")
def loginTwo(*args, **kwargs):
    print("welcome to loginTwo page")

# a = login()
# print(a)
loginTwo()











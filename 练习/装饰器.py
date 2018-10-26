#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
def func1(test):
    def func(*args, **kwargs):
        print("b")
        test()
    return func


@func1
def func():
    print("a")
func()
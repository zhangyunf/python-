#-*- coding:utf-8 -*-
#!Author:YunFei Zhang

_username = "zhangsan"
_password = "123456"
count = 0
while count < 3:
    username = input("your name is:")
    password = input("your password is:")
    if _username == username  and _password == password:
        print("Welcome %s login!", username)
        break
    elif username != _username or password != _password:
        print("Invalid username or password")
        count += 1
else:
    print("your account is locked!")

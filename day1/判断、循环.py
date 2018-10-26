#-*- coding:utf-8 -*-
#!Author:YunFei Zhang

'''
_username = "zhangsan"
_password = "123456"
username = input("username:")
password = input("password:")

if _username == username and _password == password:
    print("Welcome user %s login..." % username)
elif _username != username or _password != password:
    print("Invalid username or password")
else:
    print("Invalid username and password")
'''
'''
count = 0
while count <= 3:
    print(count)
    count += 1
else:
    print(count)

'''

_username = "zhangsan"
_password = "123456"
while True:
    username1 = input("username:")
    password1 = input("password:")
    if _username == username1 and _password == password1:
        print("Welcome user %s login..." % username1)
        # 提前跳出循环
        break
    elif _username != username1 or _password != password1:
        print("Invalid username or password")
        continue#进入下次循环


'''
for i in range(10, 1):
    print("loop", i)
'''
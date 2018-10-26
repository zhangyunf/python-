#-*- coding:utf-8 -*-
#!Author:YunFei Zhang

#输入input()
username = input("your name is:")
password = input("your password is:")
#输出print()
#格式化输出
info = '''
----info of-------
username: %s
password:%s
''' % (username, password)

info1 = '''
----info of-------
username: {username}
password:{password}
'''.format(username=username, password=password)
print(info1)
info3 = '''
----info of-------
username: {0}
password:{1}
'''.format(username, password)
print(info3)
#密文
import getpass
pas = getpass.getpass("password:")

#-*- coding:utf-8 -*-
#!Author:YunFei Zhang

username = input("your name is:")
password = input("your password is:")

info = "----info----\n" + "username:" +username+"\npassword:" + password

info1 = '''
---info---
username:%s
password:%s
''' % (username, password)

info2 = '''
----info-----
username:{username}
password:{password}
'''.format(username=username, password=password)

info3 = '''
----info----
username:{0}
password:{1}
'''.format(username, password)
print(info, info1, info2, info3)
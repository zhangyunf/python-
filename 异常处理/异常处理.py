#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei

# try语句处理
'''
try:
    aa
except Exception as error:
    print(error)
else:
    print("正确")
finaly:
    print('清理处理')
'''

# raise 主动触发异常
''''
try:
    raise NameError('没有进行命名')

except Exception as error:
    print(error)
'''


# 自定义异常
class MyException(BaseException):
     def __init__(self, msg):
         super(MyException, self).__init__()
         self.msg = msg

     def __str__(self):
         return self.msg

try:
    raise MyException('定义错误')
except MyException as error:
    print(error)

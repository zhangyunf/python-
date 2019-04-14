#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei

import time


# 返回处理器时间，3.3开始已废弃，改成time.process_time()测量处理器运算时间，不包括sleep时间，不稳定，mac上测不出来
print(time.clock())
print(time.process_time())

# 返回与utc(协调世界时)时间的时间差，以秒计算
print(time.altzone)

# 返回时间格式"Fri Aug 19 HH:mm:DD YYYY"
print("返回时间格式:%s", time.asctime())

'''
返回本地时间的struct time 对象格式
[time.struct_time(tm_year=2019, tm_mon=4, tm_mday=14, tm_hour=21, 
tm_min=15, tm_sec=1, tm_wday=6, tm_yday=104, tm_isdst=0)]
'''
print("返回本地时间struct time对象格式:%s", time.localtime())

# 返回utc时间的srtuct时间的对象格式
print("返回utc的struct时间的对象格式%s", time.gmtime(time.time()))

# 返回本地的时间格式
print(time.asctime(time.localtime()))

# 返回同上的时间格式
print(time.ctime())

# 日期字符串 转成 时间戳
string_2_struct = time.strptime("2019/4/14", "%Y/%M/%d")
print("第一种转化方式struct:%s", string_2_struct)

string_2_stamp = time.mktime(string_2_struct)
print("struct格式时间转化成时间戳:%s", string_2_stamp)

# 时间戳转化成字符串格式

# 将utc时间戳转换成struct_time格式
print(time.gmtime(time.time() - 86640))
# 将utc struct_time格式转成指定的字符串格式
print(time.strftime("%Y-%m_%d %H:%M:%S", time.gmtime()))

# 时间加减

import datetime

# 返回 YYYY:mm:DD HH:MM:SS
print(datetime.datetime.now())

# 时间戳直接转成日期格式 YYYY:mm:DD
print(datetime.date.fromtimestamp(time.time()))

# 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(3))

# 当前时间-3天
print(datetime.datetime.now() - datetime.timedelta(-3))

# 当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(hours=3))

# 当前时间+30分钟
print(datetime.datetime.now() + datetime.timedelta(minutes=30))




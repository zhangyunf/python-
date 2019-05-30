#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import threading
import time

def addNum():
    global num # 在每个线程中都获取这个全局变量
    print('----get num---', num)
    time.sleep(4)
    # 修改数据前加锁
    lock.acquire()
    num = num + 1
    # 修改完成后释放
    lock.release()

num = 1
thread_list = []
lock = threading.Lock()# 生成全局锁

for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)
# 等待所有线程都执行完毕
for t in thread_list:
    t.join()

print('final num:', num)
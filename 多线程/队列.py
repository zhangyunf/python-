#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import threading
import queue

def producer():
    for i in range(10):
        # 放入
        q.put("骨头 %s" % i)
    print("开始等待")
    q.join()
    print("取完了")

def consumer(n):
    while q.qsize() > 0:
        # 获取个数
        print("%s 取到 " % n, q.get())
        q.task_done()# 告知这个任务执行完了

q = queue.LifoQueue()
p = threading.Thread(target=producer)
p.start()
c1 = consumer("aa")
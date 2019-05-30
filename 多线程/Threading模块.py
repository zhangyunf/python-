#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import threading
import time

def sayhi(num):
    # 定义每个线程要运行的函数
    print("runniing on number:%s" % num)
    time.sleep(3)

if __name__ == '__main__':
    t1 = threading.Thread(target=sayhi, args=(1,))
    t2 = threading.Thread(target=sayhi, args=(2,))

    # 开启线程
    t1.start()
    t2.start()

    # 获取线程名称
    print(t1.getName())
    print(t2.getName())
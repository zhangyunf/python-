#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
'''
互斥锁 同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据 ，比如厕所有3个坑，
那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去。
'''
import threading, time
def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread:%s \n" % n)
    semaphore.release()

if __name__ == '__main__':
    num = 0
    # 设置允许最多同时运行的线程数量
    semaphore = threading.BoundedSemaphore(5)
    for i in range(20):
        t = threading.Thread(target=run, args=(1, ))
        t.start()
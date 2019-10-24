#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import threading
import time

num = 0
con = threading.Condition()

class Producer(threading.Thread):
    """生产者"""
    def run(self):
        global num
        # 获取锁
        con.acquire()
        while True:
            num += 1
            print('生产了1个，现在有{0}个'.format(num))
            time.sleep(1)
            if num >= 5:
                print('已达到5个，不再生产')
                # 唤醒消费者
                con.notify()
                # 等待-释放锁；被唤醒-获取锁
                con.wait()
        con.release()

class Customer(threading.Thread):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.money = 7

    def run(self):
        global num
        while self.money > 0:
            con.acquire()
            if num <= 0:
                print('没货了，{0}通知生产者'.format(threading.current_thread().name))
                con.notify()
                con.wait()
            self.money -= 1
            num -= 1
            print('{0}消费了1个，剩余1个'.format(threading.current_thread().name, num))
            con.release()
            time.sleep(1)
        print('{0}没钱了-回老家'.format(threading.current_thread().name))

if __name__ == '__main__':
    p = Producer(daemon=True)
    c1 = Customer(name='Customer-1')
    c2 = Customer(name='Customer-2')
    p.start()
    c1.start()
    c2.start()
    c1.join()
    c2.join()

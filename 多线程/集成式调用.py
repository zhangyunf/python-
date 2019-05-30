#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import threading
import time

class MyThreading(threading.Thread):

    def __init__(self, num):
        super(MyThreading, self).__init__()
        self.num = num

    def run(self):
        print("running on number %s" % self.num)
        time.sleep(3)

if __name__ == '__main__':
    t1 = MyThreading(1)
    t2 = MyThreading(2)

    t1.start()
    t2.start()
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import threading
import queue
import time,random
q = queue.Queue()
def Producer(name):
    count = 0
    while count < 20:
        time.sleep(random.randrange(3))
        q.put(count)
        print('producer %s has produced %s baozi' % (name, count))
        count += 1

def Consumer(name):
    count = 0
    while count < 20:
        time.sleep(random.randrange(4))
        if not q.empty():
            data = q.get()
            print(data)
            print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' %(name, data))
        else:
            print('----no baozi anymore')
        count += 1
p1 = threading.Thread(target=Producer, args=("a", ))
c1 = threading.Thread(target=Consumer, args=("b", ))
p1.start()
c1.start()
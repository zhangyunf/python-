#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
from threading import Timer
import time

def hello():
    print("hello world")

t = Timer(30, hello)
t.start()
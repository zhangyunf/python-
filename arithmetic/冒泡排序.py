#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
from arithmetic.runTime import run_time


@run_time
def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

@run_time
def bubble_sort_2(li):
    for i in range(len(li) - 1):
        exchange = li[i]
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]



if __name__ == '__main__':
    data = list(range(1000, 1, -1))
    bubble_sort(data)




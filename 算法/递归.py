#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
'''
题目描述
求1！+2！+3！+……+n！

输入描述
输入n的值（整数）

输出描述
输出1至n的阶乘的累加和
n!+(n-1)!循环套上n*(n-1)的循环
'''

def Nn(n):
    if n == 1:
        return 1
    def N2(n):
        if n == 1:
            return 1
        return N2(n-1)*n
    return Nn(n-1)+N2(n)
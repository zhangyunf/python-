#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
a = [1, 3, 4, 2, 3]

def Nn(n):
    if n == 1:
        return 1
    def N2(n):
        if n ==1:
            return 1
        return N2(n-1)*n
    return Nn(n-1)+N2(n)

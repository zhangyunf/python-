#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei

# 随机数
import random

# 随机生成随机数
print(random.random())

# 随机生成1，2整数
print(random.randint(1, 2))

# 随机生成小数
print(random.uniform(1, 2))

# 随机生成1， 10范围内的整数（顾头不顾尾.遍历时按顺序取值，最后一个参数可以加步长
print(random.randrange(1, 10))

# 随机字符串
print(random.choice('dafads'))

# 多个字符串中随机生成指定数量的随机字符
print(random.sample('fasfafsdfasd', 5))

# 打乱排序
items = [1, 2, 3, 4]
print(random.shuffle(items))

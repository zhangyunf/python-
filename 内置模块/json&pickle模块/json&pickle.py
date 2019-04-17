#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei

'''
用于序列化的两个模块
json:用于字符串和python数据类型间进行转换
pickle:用于python特有的类型和python的数据类型之间进行转换
Json模块提供了四个功能：dumps、dump、loads、load
json.dumps:将字典转化为字符串。是将一个Python数据噢诶性的列表进行json格式编码。
json.dump:读取json文件，并进行json格式编码
json.loads:将json格式数据转换为字典。
json.load:读取json格式数据，并转化为字典。


pickle模块提供了四个功能dumps、dump、loads、load
dumps:数据--->字符串
dump:数据---->字符串，并写入文件
loads:将pickle数据转换为python数据结构
load:从文件中读取数据，并转换为python的数据结构
'''
import pickle

data = {"k1": 123, "k2": "hello"}
data1 = '{"k1": 123, "k2": "hello"}'

# pickle.dumps 将数据通过特殊的形式转换为只有python语言认识的字符串
p_str = pickle.dumps(data)
# pickle.loads 将pickle数据转化为python数据结构
print(type(pickle.loads(p_str)))

# pickle.dump 将数据通过特殊的形式转化为只有python语言认识的字符串，并写入文件

with open("a.txt", "wb") as file:
    pickle.dump(data, file)

# pickle.load 从数据文件中读取数据，并转化成python的数据格式
with open("a.txt", "rb") as file:
    data2 = pickle.load(file)
    print(data2)




import json
# json.dumps 将数据通过特殊的形式转换为所有程序语言都认识的字符串
print(type(json.dumps(data)))

# json.loads 字符串---->python形式
print(type(json.loads(data1)))

with open("a.json", "r") as file:
    data_json = json.load(file)
    print("json.load", type(data_json), data_json)

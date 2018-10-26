#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
#第一种
'''
module_test = __import__("module_test.module")#这是解释器自己内部使用的,实际上是导入了module_test
obj = module_test.module.log()
'''
#第二种
import importlib
module = importlib.import_module("module_test.module")
print(module.log())
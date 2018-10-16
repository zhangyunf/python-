#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
#http://www.cnblogs.com/luotianshuai/articles/5735051.html
#查看系统编码格式
import sys
print(sys.getdefaultencoding())
s = "你好"
s_to_gbk = s.encode("gbk")
print(s_to_gbk)
print(s.encode())
gbk_to_utf8 = s_to_gbk.decode("gbk").encode("utf-8")
print(gbk_to_utf8)
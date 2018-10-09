#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
'''
字典
'''
info = {
    "stu1101": "TengLan Wu",
    "stu1102": "LongZe luoLa",
    "stu1103": "XiaoZe Maliya",
}
print(info["stu1101"])#根据key值获取value值
info["stu1101"] = "武藤兰"#修改value值
info["stu1104"] = "CangJingkong"#添加，如果有就修改，如果没有就添加
#del info["stu1101"]#删除
# info.pop("stu1101")#删除
# info.popitem()#随机删除
print(info.get("stu1103"))#查找，有就返回，没有返回None
print("stu1103" in info)#查找


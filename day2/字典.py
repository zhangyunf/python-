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

catalog = {
    "欧美": {
        "www.aaa.com": ["很多免费的,世界最大的", "质量一般"],
        "www.bbb.com": ["很多免费的,也很大", "质量比aaa高点"],
        "ccc.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
        "ddd.com": ["质量很高,真的很高", "全部收费,屌比请绕过"]
    },
    "日韩": {
        "www.ggg.com": ["质量怎样不清楚,个人已经不喜欢日韩范了", "听说是收费的"]
    },
    "大陆": {
        "www.ttt.com": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
    }
}
catalog["大陆"]["www.ttt.com"][1] = "可以在国内搭建服务器"
catalog.setdefault("台湾", {"www.sogou.com":[1, 2]})#增加键值对
a = {
    "a": 1
}
b = {
    "a": 1,
    "2": 2
}
a.update(b)#合并,重复的覆盖
c = a.fromkeys([6, 7, 8], [1, {"name": "alex"}])#重新创建一个字典,value只是个指针，赋值给三个value
print(c)
#循环
for key in info:
    print(key, info[key])
for k, v in info.items():
    print(k, v)
'''
三级菜单
'''
data = {
    "北京": {
        "昌平": {
            "沙河": ["oldboy", "text"],
            "天通苑":["链家地产", "我爱我家"]
        },
        "朝阳": {
            "望京": ["奔驰", "陌陌"],
            "国贸": ["CICC", "HP"],
            "东直门": ["Advent", "飞信"]
        },
        "海淀": {

        },
    },
    "山东": {
        "德州": {},
        "青岛": {},
        "济南": {},
    },
    "广东": {
        "东莞": {},
        "常州": {},
        "佛山": {},

    }
}
def printValue(data1):
    pass


# while True:
#     for k in data:
#         print(k)
#     choose = input("选择进入1》》：")
#     if choose in data:
#         while True:
#             for k in data[choose]:
#                 print(k)
#             choose2 = input("选择进入2》》：")
#             if choose2 in data[choose]:
#                 while True:
#                     for i3 in data[choose][choose2]:
#                         print()


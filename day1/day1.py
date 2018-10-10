import copy
'''
三元运算
'''
# a, b, c = 4, 2, 3
# d = a if a > b else c
# d = a if a < b else c
# print(d)
'''
string与bytes转化
'''
# msg = "我爱北京天安门"
# print(msg.encode("utf-8"))
# print(msg.encode("utf-8").decode(encoding="utf-8"))
'''
列表
'''
#names = "ZhangYang GuyunXiangpeng XuLiangChen"
# names = ["ZhangYang", "GuYun", "XiangPeng", "XuLiangchen", "ChenRonghua"]
# print(names) #打印整个列表
# print(names[0]) #获取指定下标的数据
# print(names[1: 3])#切片，顾头不顾尾
# print(names[-1])#最后一个
# names.append("LeiHaidong")#添加到最后一位
# names.insert(1, "ChenRonghua")#放入到指定位置
#delete
# names.remove("ZhangYang")
# names.pop()#删除最后一个
#获取指定数据的下标
# print(names.index("GuYun"))
#统计有多少个同名
# print(names.count("ChenRonghua"))
#清空
# names.clear()
#翻转
# names.reverse()
#排序
#names.sort()
#并购
# names2 = [1, 2, 3, 4]
# names.extend(names2)
# name2 = names.copy()
# name3 = copy.deepcopy(names)
#循环
# for i in names:
#     print(i)
#
# range(1, 10, 2)#从1开始到10，每隔2个
#print(names[0:-1:2])#从0到最后一个，每隔一个
# print(names, "\n", names2)
#三种浅copy方式
# person = ['name', ['a', 100]]
# pl = person.copy()
# pl1 = copy.copy(person)
# pll = person[:]

'''
元组：只读列表 ()
      只有两个方法，count, index
'''
# names = ("alex", "jack")
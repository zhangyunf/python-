'''
集合
'''

l1 = [1, 4, 6, 8, 1, 7]
list_1 = set(l1)#去重
list_2 = set([1, 3, 4, 5, 6, 7, 2, 4, 2, 45])
'''
print(list_1, list_2)
print(list_1.intersection(list_2))#求交集
print(list_1.union(list_2))#并集
print(list_1.difference(list_2))#差集
print(list_1.issubset(list_2))#判断是否是list_2的子集
print(list_1.issuperset(list_2))#判断是否是父集
print(list_1.symmetric_difference(list_2))#对称差集
'''
'''
print(list_1 & list_2)#intersection
print(list_1 | list_2)#union
print(list_1 - list_2)#difference
print(list_1 ^ list_2)#symmetric_difference对称差集
'''
list_1.add(99)#添加
list_1.update([22, 44])#添加多项
list_1.remove(22)#删除，如果不存在会报错
list_1.pop()#删除任意
list_1.discard(44)#如果有删除，如果没有不做任何处理
print(44 in list_1)#判断是否存在list_1里
print(44 not in list_1)#不存在
print(list_1)

#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
'''
有一组“+”和一组“-”，要求“+”在左，“-”在右
'''

def sortOne(data):
    plusList = []
    minusList = []
    for i in data:

        if i == "+":
            plusList.append(i)
        else:
            minusList.append(i)
    plusList.extend(minusList)
    return plusList
data = ['-', '-', '+', '+', '+','-', '+','-', '+','-','-']

print(sortOne(data))

'''
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？ 
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列
'''
sumone = 0
for i in range(1, 5, 1):
    for j in range(1, 5, 1):
        for k in range(1, 5, 1):
            if i != j & i != k & j != k:
                print()
                sumone = sumone + 1
                result = (i*100) + (j*10) + k
                print(result)
print(sumone)
'''
列表排序
'''
list1 = [1, 4, 7, 8, 9, 5, 8, 5, 4, 5, 6, 7, 8, 6, 6, 5, 5, 1, 2, 45, 54]
list1.sort()
print(list1)
'''
一行代码实现1--100之和
'''
a =sum(range(0, 101))
print(a)
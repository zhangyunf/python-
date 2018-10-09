#-*- coding:utf-8 -*-
#!Author:YunFei Zhang

'''
练习题
需求：1、启动程序后，让用户输入工资，然后打印商品列表
      2、允许用户根据商品编号购买商品
      3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
      4、可随时退出，退出时，打印已购买商品和余额
'''
class goods(object):
   def __init__(self, productNum, productName, price):
       self.__productNum = productNum
       self.__productName = productName
       self.__price = price
   def setProductNum(self, productNum):
       self.__productNum = productNum
   def getProductNum(self):
       return self.__productNum
   def setProductName(self, productName):
       self.__productName = productName
   def getProductName(self):
       return self.__productName
   def setPrice(self, price):
       self.__price = price
   def getPrice(self):
       return self.__price
   def description(self):
       print(self.__productNum, self.__productName, self.__price, "\n")


class main():
    #商品列表
    productList = [goods(1, "IPhone", 5000),
                   goods(2, " MacPro", 12000),
                   goods(3, "IPhone XS Mac", 9000)]
    #输入工资
    salary = int(input("please input your salary!\n"))
    #创建购物车列表
    shoppingCart = []
    #循环标识
    sign = True
    while sign:
        # 打印商品
        for trade in productList:
            trade.description()
        # 选择商品编号
        productNum = input("please input prdoct code!\n")
        # 随时退出
        if productNum == "q":
            for good in shoppingCart:
                good.description()
            print("your balance is", salary)
            sign = False
            break
        else:
            productNum = int(productNum)
        product = productList[productNum - 1]

        # 判断余额
        if salary < product.getPrice():
            print("prompt of insufficient balance!")
        else:
            shoppingCart.append(productList[productNum - 1])
            salary = salary - productList[productNum - 1].getPrice()
if __name__ == "__main__":
    main()





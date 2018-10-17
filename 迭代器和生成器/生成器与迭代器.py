#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
'''
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数
元素占用的空间都白白浪费了。所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出来
后续的元素那？这样不必创建完整的list，从而节省大量的空间。在python中，这种一遍循环一遍计算的机制，成为生成器
generator
1、生成器只有在调用时才会生成相应的数据
2、生成器只保留当前位置的数据
3、只有__next__()方法。获取下一个数据。
'''

#1、列表生成器
'''
lis = (i*2 for i in range(10))#只返回一个地址，只有访问的时候才会生成
print(lis)#打印lis地址
print(lis.__next__())#访问第一个数据，所以只生成第一个值，并输出
'''
#2、给函数变成生成器。
# 斐波拉契数列：除第一个和第二个数外，任意一个数都可由两个数相加得到[1,1,2,3,4,8,13,21]
'''
def fib(max):
    n, a, b, = 0, 0, 1
    while n < max:
        #print(b)
        yield b#想要在哪里中断，就放在哪里。即保存了函数的中断状态。
        a, b = b, a + b
        n = n + 1
    return "done"#异常处理

        
print(fib(10))
f = fib(10)
print(f.__next__())
print("====")
for i in f:
    print(i)
'''
#3、可以通过yield,实现并行效果
#例如等着吃东西的时候，玩着手机的同时，东西也在做着。
'''
def eat(food):
    print("%s来了" % food)
    while True:
        person = yield
        print("%s 吃了 %s" % (person, food))

print("饺子")
print("玩手机")
c = eat("饺子")#实例化生成器
c.__next__()#启动生成器

c.send("张三")#返回到yield处,并向yield传值
'''
'''
def consumer(name):
    print("来盘饺子！")
    c = eat("饺子")
    print("等着我无聊，玩会手机！")
    c.__next__()
    c.send(name)
d = consumer("张三")
'''
'''
可迭代对象（Iterable）：可以直接作用于for循环的对象。
1、集合数据类型：如list、tuple、dict、set、str等。
2、生成器
判断是否为可迭代对象：isinstance()
迭代器（Iterator）：可以被next()函数调用并不断返回下一个值的对象
'''
'''
from collections import Iterable, Iterator

a = [1, 2, 3]
print(isinstance(a, Iterable))

b = (i for i in range(10))
print(isinstance(b, Iterator))

'''
#把可迭代对象变成迭代器iter()
'''
a = [1, 2, 3]
b = iter(a)
print(b.__next__)
'''



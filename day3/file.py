'''
文件：读模式"r",
      写模式"w",会删除原来的东西；
      追加模式"a"，在最后写入；
      "rb"：二进制文件；
      "wb":二进制写入，以二进制处理，存入的可以是别的编码的；
      "r+":读写；
      "w+":写读；

'''
#读
'''
f = open("yesterday", "r", encoding="utf-8")#句柄
data = f.read()#()中填入数字，表示读取字符的个数
print("%s" % data)
data1 = f.read()
print("----", data1)#为什么打印不出来data1那，类似光标在移动，读取完data中光标已经在最后了，所以在读data时，已经没有东西了
f.close()
'''
#追加
'''
fil = open("write", "a", encoding="utf-8")
fil.write("我爱北京天安门\n")
fil.write("天安门上太阳升\n")
fil.close()
'''
#只读前5行
# f = open("yesterday", "r", encoding="utf-8")
'''
print(f.readline())#只读一行
print(f.readlines())#以行分割，返回列表
fil.close()
'''
'''
#循环读取--low loop--占内存过大
for line in f.readlines():
    print(line.strip())

#low loop
for index, line in enumerate(f.readlines()):
    if index == 5:
        print("----分割线--------")
        break
    print(line.strip())
fil.close()
'''
'''
#一行一行的读，每次只读取一行到内存里。输出后删除。
count = 0
for line in f:
    count += 1
    if count == 6:
        break
    print(line)
fil.close()
'''
#读写(写入的话是追加)
'''
f = open("write", "r+", encoding="utf-8")
print(f.readline())
f.write("-------diao-------")
print(f.readline())
fil.close()
'''
#写读
'''
f = open("write", "w+", encoding="utf-8")
f.write("-------diao-------")
print(f.readline())
f.close()
'''
#光标位置
'''
f = open("yesterday", "r", encoding="utf-8")
print(f.tell())#返回光标的位置
print(f.readline())
f.seek(0)#光标返回原点
print(f.readline())
fil.close()
'''
#实时刷新
'''
f = open("write", "w", encoding="utf-8")
f.write("rrrr\n")
f.flush()#当写入的时候，会有个缓存，如果缓存满了才会往硬盘上写入，然后清空缓存。如果想要在缓存没有满的情况下就把现在已有的东西写入硬盘，就用此方法
fil.close()
'''
'''
import  sys,time
for i in range(50):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(1)
fil.close()
'''
#修改
'''
f = open("yesterday", "r", encoding="utf-8")
f_new = open("yesterday2.bak", "w" ,encoding="utf-8")
for line in f:
    if "如果那两个字没有" in line:
        line = line.replace("如果那两个字没有", "如果那两个字没有没有")
    f_new.write(line)
f.close()
f_new.close()
'''
#为了避免打开文件忘记关闭，可以通过管理上下文
'''
with open("yesterday", "r", encoding="utf-8") as f:
    for line in f:
        print(line)
'''
#python2.7后，with同时打开多个文件
'''
with open("yesterday", "r", encoding="utf-8") as f,\
     open("yesterday", "r", encoding="utf-8") as a:
    pass
'''
#其他
'''
f = open("write", "a", encoding="utf-8")
print(f.encoding)#文件编码格式
print(f.name)#名字
print(f.seekable())#判断光标是否能移动
print(f.readable())#判断文件是否可读
f.truncate(10)#保留10位
fil.close()
'''


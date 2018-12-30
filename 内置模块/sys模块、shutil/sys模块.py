import shutil #copy文件

#高级的文件、文件夹、压缩包处理模块
#把一个文件内容copy到另一个文件中(需要自己打开文件)
with open("a.txt", "rb") as a:
    with open("b.txt", "wb") as b:
        shutil.copyfileobj(a, b)
#复制内容（不用打开）
shutil.copyfile("b.txt", "c.txt")
#仅拷贝权限，内容、组、用户均不变
# shutil.copymode()

#拷贝
shutil.copystat()




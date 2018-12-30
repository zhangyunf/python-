import os
#获取当前的目录
# print(os.getcwd())
#切换目录
os.chdir("../")
print(os.getcwd())
#返回当前目录
# print(os.curdir)
# #获取当前目录的父目录上级目录
# print(os.pardir)
#递归的创建目录C:\a\b\c\d
# os.makedirs("path")
#移除目录
# os.removedirs("path")
#只能在当前目录下创建文件
# os.mkdir()
#删除空级目录,若目录不为空则无法删除，报错；相当于shell中的rmdir dirname
# os.rmdir()
#列出制定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.listdir()
#删除一个文件
#重命名"文件/目录"
# os.rename("oldname", "newname")
#获取文件/目录信息
# os.stat("path/filename")
#输出操作系统的特定的路径分隔符
print(os.sep)
#输出当前平台使用的行终止符
print(os.linesep)
#输出用于分割文件路径的字符串
print(os.pathsep)
#输出系统环境变量
print(os.environ)
#系统名称
print(os.name)
#运行cmdprint(os.path.dirname(r"D:\a\b\c.txt"))

print(os.system("dir"))
#返回文件的绝对路径
# print(os.path.abspath())
#分割路径和文件
# print(os.path.split())
#只取路径
# print(os.path.dirname(r"D:\a\b\c.txt"))
#只取文件
# print(os.path.basename(r"D:\a\b\c.txt"))
#判断输入的路径是否存在：Ture False
# print(os.path.exists())
#判断是否是绝对路径
# print(os.path.isabs())
#判断是否是一个存在的文件
# print(os.path.isfile())
#是否是一个存在的目录
# print(os.path.isdir())
#将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.join(r"D:", r"c"))
#返回文件的最后存取时间
print(os.path.getatime())
#返回修改时间
print(os.path.getmtime())
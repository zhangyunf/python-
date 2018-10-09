#-*- coding:utf-8 -*-
#!Author:YunFei Zhang

'''
字符串操作
'''
name = "my \tname is alex"
print(name.capitalize())#首字母大写
print(name.count("a"))#多少个a
print(name.center(50,"-"))#左右各放置20个“-”，中间是name
print(name.endswith("ex"))#判断是否是以ex结尾
print(name.expandtabs(tabsize=30))#将\t转化成30个“ ”
print(name[name.find("a"):])#find返回“a”的位置
name1 = "my name is {name} and my age is {age}"
print(name1.format(name="alex", age=23))#格式化输出
# print(name1.format_map({"name": "alex", "age": 12}))
# print("ab23".isalnum())#判断是否包含特殊字符
# print("adA".isalpha())#判断是否是纯字母
# print("1".isdecimal())#判断是否是十进制
# print("10".isdigit())#*判断是否是一个整数
# print("1A".isidentifier())#判断是否是一个合法的标识符(不能以数字、特殊字符以及空格开头)
# print("33".isnumeric())#判断是否只有数字
# print(" ".isspace())#是否是空格
# print("My Name Is".istitle())
# print("My Name Is".isprintable())#tty file, drive file
print("+".join(["1", "2", "3", "4"]))#将列表中的每个数据中间加“+”之后变成字符串
print(name1.ljust(50, "*"))#不够50位的用*补上
print(name1.rjust(50, "-"))#不够50位的在前面用-补上
print("Alex".lower())#小写
print("Alex".upper())#大写
print("\nAlex".lstrip())#去除左边的回车或空格
print("Alex\n".rstrip())#去除右边的回车和空格
print("  Alex\n".strip())#去除两边的回车和空格
p = str.maketrans("abcdef", "123456")
print("acdel".translate(p))#"p"中后面的数字对应前面的字母，然后用对应的数字替换“acdel”
print("alex li".replace("l", "L", 1))#替换，用L替换l，如果全部替换则不用写“1”
print("alex li".rfind("l"))#找到对应字母的下标，对应find
print("al ex lil".split(" "))#用“ ”分割字符串，返回列表
print("1+2\n+3+4".splitlines())#以“\n”分割字符串
print("Alex li".swapcase())#大小写互换
print("lex li".title())#每个单词首字母大写


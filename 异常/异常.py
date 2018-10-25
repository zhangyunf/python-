#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
name = ["a", "b"]
data = {}
try:
    #KeyError
    #data["name"]
    #IndexError
    #name[3]
    #无错
    name[0]

except (IndexError, KeyError) as IE:#如果出现两种错误的时候做同样的处理
    print("溢出 ", IE)
except KeyError as KE:
    print("没有key", KE)
except Exception as e:#判断所有的错误
    print(e)
else:#没有错的时候执行
    print("一切正常")
finally:#有没有错都执行
    print("结束")


















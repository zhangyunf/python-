import time
#时间戳-1970
print(time.time())
#元组
print(time.localtime())
#等待
time.sleep(1)
#时间戳---元组
#标准时间
print(time.gmtime())
#传入s
print(time.gmtime(4324324324324))
#获取元组中的时间数据
t = time.localtime()
print(t.tm_year)
print("this is 1973 day:%d" % t.tm_yday)
#元组---时间戳
print(time.mktime(t))
#元组----字符串
print(time.strftime("%Y-%m-%d %H:%M:%S", t))
#字符串---元组
print(time.strptime("2018-12-11 23:11:46", "%Y-%m-%d %H:%M:%S"))
#元组----字符串
print(time.asctime())
#时间戳----字符串
print(time.ctime(time.time()))

import datetime
#年月日
print(datetime.date)
#年月日时分秒
print(datetime.datetime.now())#获取当前时间
print(datetime.datetime.now() + datetime.timedelta())#以前和未来的时间
print(datetime.datetime.now() + datetime.timedelta(3))#从现在开始加三天
print(datetime.datetime.now() + datetime.timedelta(hours=-3))#从3小时之前



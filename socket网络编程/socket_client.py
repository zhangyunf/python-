#-*- coding:utf-8 -*-
#!Author:YunFei Zhang

import socket
client = socket.socket()#申明socket类型，同时生成socket连接对象
client.connect(("localhost", 9999))
while True:
    msg = input(">>:").strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode("utf-8"))
    data = client.recv(1024)
    print(data)
client.close()





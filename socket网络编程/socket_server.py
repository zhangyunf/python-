#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
import socket

server = socket.socket()
server.bind(("localhost", 9999))#绑定要监听的端口、
server.listen(5)  # 监听
while True:
    print("我要开始等电话了")
    conn, addr = server.accept()  # 等数据,conn连接实例，addr地址
    print(conn, addr)
    while True:
        data = conn.recv(1024)  # 接受数据
        print(data)
        if not data:
            print("无数据传输")
            break
        print(data.decode())
        conn.send(data.upper())
server.close()
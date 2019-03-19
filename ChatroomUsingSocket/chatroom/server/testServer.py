#!/usr/bin/env python
# coding: utf-8
# author: Xiao Guaishou

import socket
from threading import currentThread, Thread
import User
import Chatroom

# 创建一个基于IPv4和TCP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
s.bind(('127.0.0.1', 9999))
s.listen(5)  # 调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量
print('Waiting for connection...')


# def tcplink(sock, addr):
#     print('Accept new connection from %s:%s...' % addr)
#     sock.send(str('欢迎你进入python聊天开发的行业!').encode())  # 连接建立后，服务器发送一条欢迎消息
#     while True:
#         data = sock.recv(1024)
#         if not data or data.decode('utf-8') == 'exit':  # 判断接受的数据是否为空
#             break
#         sock.send(('你好,你刚刚给我说了： %s!' % data.decode('utf-8')).encode('utf-8'))
#     sock.close()
nameList = ['小明', '小红', '小刚','小华','小李','小军','老李']
count = 0
chatroom = Chatroom.Chatroom()
t = Thread(target=chatroom.toChat)     # 在新线程中创建一个聊天室:
t.start()
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    user = User.User(nameList[count],sock) #实例化一个用户类
    chatroom.addUser(user)
    if chatroom.getUserCount() == 0:
        t.join()
        print('exit server')
        break
    count += 1
    

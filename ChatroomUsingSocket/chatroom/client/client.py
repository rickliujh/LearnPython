#! /usr/bin/python
# -*- coding: utf-8 -*-
import socket
from threading import currentThread, Thread
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def getMessage(sock, s):
    s.send(None)
    while True:
        data = sock.recv(1024)
        # print("接收到了服务器端发送过来的数据：{0}".format(bytes(data).decode()))
        s.send(data)
    s.close()

def sendMessage(sock):
    while True:
        data = yield
        if not data:
            yield
        print("{0}".format(bytes(data).decode()))
        strInput = input("我: ")
        sock.sendall(strInput.encode())

def check_tcp_status(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    print("connecting to %s:%s" % server_address, port)
    sock.connect(server_address)

    # while True:
    #     await getMessage(sock)
    #     await sendMessage(sock)

    # message = input("pleas input: ")
    # print("Sending '%s'" % message)
    #
    # sock.sendall(message.encode())
    # print("Closing socket")
    s = sendMessage(sock)
    getMessage(sock, s)
        # data = sock.recv(1024)
        # time.sleep(1)
        # if not data:
        #     break
        # print("接收到了服务器端发送过来的数据：{0}".format(bytes(data).decode()))
        # strInput = input("请输入你想说的话给服务器：")
        # sock.sendall(strInput.encode())


    sock.close()


if __name__ == "__main__":
    print(check_tcp_status("127.0.0.1", 9999))
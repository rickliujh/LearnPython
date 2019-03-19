import time
import hashlib


class User(object):
    __slots__ = ('__userName', '__userHash', '__sock')

    def __init__(self, userName, sock):
        self.__userName = userName
        self.__userHash = hash(userName + str(time.time()))
        self.__sock = sock
        self.__sock.settimeout(0.01)

    def getUserName(self):
        return self.__userName

    def getUserHash(self):
        return self.__userHash

    def setSock(self, sock):
        self.__sock = sock

    def getSock(self):
        return self.__sock

    def getMessage(self):
        data = None
        try:
            data = self.getUserName() + ": " + self.__sock.recv(1024).decode('utf-8')
        finally:
            return data

    def sendMessage(self, message):
        try:
            self.__sock.send(str(message).encode('utf-8'))
        finally:
            return

    def getSockPeerName(self):
        ip, port = None, None
        try:
            ip, port = self.__sock.getpeername()
        finally:
            return (ip, port)
        return

    def closeSock(self):
        self.__sock.shutdown(2)
        self.__sock.close()

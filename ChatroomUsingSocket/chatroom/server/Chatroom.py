from threading import currentThread, Thread
import time

class Chatroom(object):
    __slots__ = ('__userList', '__userCount')

    def __init__(self):
        self.__userList = []
        self.__userCount = 0
        print('Create new chatroom')

    def addUser(self, user):
        self.__userList.append(user)
        self.__userCount += 1
        self.welcomeMessage(user)

    def getUserCount(self):
        return self.__userCount

    def welcomeMessage(self, user):
        ip, port = user.getSockPeerName()
        print('Accept new connection from %s:%s...' % (ip, port))
        user.sendMessage('你好! 用户: %s | %s:%s \n欢迎来到聊天室 当前共有%s人' %
                         (user.getUserName(), ip, port, self.__userCount))

    def toChat(self):  
        while True:
            s = self.sendUserMessage()
            g = self.getUserMessage(s)
            self.eachUser(g)


    def getUserMessage(self, s):
        s.send(None)
        while True:
            user = yield 
            print('get user: '+user.getUserName()+" | %s:%s" % user.getSockPeerName())
            data = user.getMessage()
            if not data:
                continue
            s.send((user, data))
        s.close()
            

    def sendUserMessage(self):
        while True:
            currUser, data = yield 
            for user in self.__userList:
                print('send user: '+user.getUserName()+" | %s:%s" % user.getSockPeerName())
                if user is currUser:
                    continue
                    # user.sendMessage('')
                user.sendMessage(data)
                

    def eachUser(self, g):
        g.send(None)
        for user in self.__userList:
            print('each user: '+user.getUserName()+" | %s:%s" % user.getSockPeerName())
            g.send(user)
        g.close()
            

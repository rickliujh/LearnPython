import time
import hashlib


class TransData(object):
    __slots__ = ('__userName__', '__userHash__',
                 'type', '__toUserHash__', 'data')

    def __init__(self, userName):
        self.__userName__ = userName  # 用户名
        self.__userHash__ = hash(userName + str(time.time()))  # 用户唯一标示
        self.data = ''  # 聊天数据
        self.type = 1  # type=1 单独聊天 | type=2 群聊
        self.__toUserHash__ = ''

    def getUserName(self):
        return self.__userName__

    def getUserHash(self):
        return self.__userHash__

    def toString(self):
        return "$userName={0}$userHash={1}$type={2}$toUserHash={3}$data={4}".format(
            self.__userName__,
            self.__userHash__,
            self.type,
            self.__toUserHash__,
            self.data
        )

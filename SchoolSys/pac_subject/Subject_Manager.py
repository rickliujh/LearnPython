# -*- coding: UTF-8 -*-
from pac_DB_Common import DB_Manager
from pac_subject import Subject

class Subject_Manager(object):
    def __init__(self):
        self.__data = {}
        self.dbManager = DB_Manager.Subject_DB()

    '添加一个课程的信息到课程数据库里边'
    def add_subject(self, subject):
        if isinstance(subject, Subject.Subject):
            # self.__data.update({subject.code:subject})
            self.dbManager.add_subject(subject)
            self.__data = self.dbManager.get_all_subject()

    '对外返回整个课程信息的数据库'
    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    '查找是否已经存在相同课程代码的课程'
    def is_exist(self, code):
        if code != '':
            if len(self.dbManager.get_subject_by_code(code)) > 0:
                result = True
            else:
                result = False
        else:
            result = False
        return result

    '根据课程代码查找课程信息'
    def search_subject(self, code):
        if code != '':
            if self.__data.get(code) != None:
                return self.__data.get(code)

    def get_subject_by_code(self, code):
        self.__data = self.dbManager.get_subject_by_code(code)
        obj = self.search_subject(code)
        return  obj


    # '根据课程代码，从课程数据库里边删除该课程的信息'
    # def delete_subject(self, code):
    #     if code != '':
    #         if self.__data.get(code) != None:
    #             self.__data.pop(code)

    '输出全部课程的信息'
    def show_all_subject(self):
        self.__data = self.dbManager.get_all_subject()

        if len(self.__data) > 0:
            print("**********************************************************************")
            for key in self.__data:
                obj = self.__data[key]
                print("课程代码:{0}    |课程名称:{1}"
                .format(obj.code, obj.name))
            print("**********************************************************************")

        else:
            print("数据库里边还没有课程信息，请先添加课程信息到内存数据库！")


    '根据课程代码输出指定课程的信息'
    def show_subject(self, code):
        self.__data = self.dbManager.get_subject_by_code(code)
        obj = self.search_subject(code)
        print("**************************************************************************")
        print("课程代码:{0}    |课程名称:{1}"
                .format(obj.code, obj.name))
        print("**************************************************************************")

    '根据课程代码删除指定的'
    def delete_subject(self, code):
        # self.__data.pop(code)
        self.dbManager.delete_subject(code)
        self.__data = self.dbManager.get_all_subject()
        print("课程代码为：{0}的课程信息删除完毕！".format(code))


    '更改课程信息'
    def edit_subject(self, code, obj):
        # self.__data[code] = obj
        self.dbManager.edit_subject(obj)

    '判断课程数据库是否为空'
    def is_empty(self):
        if len(self.__data) > 0:
            return False
        else:
            return True
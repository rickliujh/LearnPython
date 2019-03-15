# -*- coding: UTF-8 -*-
from pac_DB_Common import DB_Manager
from pac_teacher import Teacher

class Teacher_Manager(object):
    def __init__(self):
        self.__data = {}
        self.dbManager = DB_Manager.Teacher_DB()

    '添加一个教师的信息到教师数据库里边'
    def add_teacher(self, teacher):
        if isinstance(teacher, Teacher.Teacher):
            # self.__data.update({teacher.code:teacher})
            self.dbManager.add_teacher(teacher)
            self.__data = self.dbManager.get_all_teacher()

    '对外返回整个教师信息的数据库'
    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    '查找是否已经存在相同教师代码的教师'
    def is_exist(self, code):
        if code != '':
            if len(self.dbManager.get_teacher_by_code(code)) > 0:
                result = True
            else:
                result = False
        else:
            result = False
        return result

    '根据教师代码查找教师信息'
    def search_teacher(self, code):
        if code != '':
            if self.__data.get(code) != None:
                return self.__data.get(code)

    def get_teacher_by_code(self, code):
        self.__data = self.dbManager.get_teacher_by_code(code)
        obj = self.search_teacher(code)
        return  obj


    # '根据教师代码，从教师数据库里边删除该教师的信息'
    # def delete_teacher(self, code):
    #     if code != '':
    #         if self.__data.get(code) != None:
    #             self.__data.pop(code)

    '输出全部教师的信息'
    def show_all_teacher(self):
        self.__data = self.dbManager.get_all_teacher()

        if len(self.__data) > 0:
            print("**********************************************************************")
            for key in self.__data:
                obj = self.__data[key]
                print("教师代码:{0}    |教师名称:{1}    |学校代码:{2}"
                .format(obj.code, obj.name, obj.school_code))
            print("**********************************************************************")

        else:
            print("数据库里边还没有教师信息，请先添加教师信息到内存数据库！")


    '根据教师代码输出指定教师的信息'
    def show_teacher(self, code):
        self.__data = self.dbManager.get_teacher_by_code(code)
        obj = self.search_teacher(code)
        print("**************************************************************************")
        print("教师代码:{0}    |教师名称:{1}    |学校代码:{2}"
                .format(obj.code, obj.name, obj.school_code))
        print("**************************************************************************")

    '根据教师代码删除指定的'
    def delete_teacher(self, code):
        # self.__data.pop(code)
        self.dbManager.delete_teacher(code)
        self.__data = self.dbManager.get_all_teacher()
        print("教师代码为：{0}的教师信息删除完毕！".format(code))


    '更改教师信息'
    def edit_teacher(self, code, obj):
        # self.__data[code] = obj
        self.dbManager.edit_teacher(obj)

    '判断教师数据库是否为空'
    def is_empty(self):
        if len(self.__data) > 0:
            return False
        else:
            return True
# -*- coding: UTF-8 -*-
import os
from pac_class import Class
from pac_DB_Common import DB_Manager
class Class_Manager(object):
    def __init__(self):
        self.__data = {}
        self.dbManager = DB_Manager.Class_DB()

    '添加一所班级的信息到班级数据库里边'
    def add_class(self, classes):
        if isinstance(classes, Class.Class):
            self.dbManager.add_class(classes)
            self.__data = self.dbManager.get_all_class()

    '对外返回整个班级信息的数据库'
    def get_data(self):
        return self.__data

    '查找是否已经存在相同班级代码的班级'
    def is_exist(self, code):
        if code != '':
            if len(self.dbManager.get_class_by_code(code)) > 0:
                result = True
            else:
                result = False
        else:
            result = False
        return result

    '根据班级代码查找班级信息'
    def search_class(self, code):
        if code != '':
            if self.__data.get(code) != None:
                return self.__data.get(code)

    def get_class_by_code(self, code):
        self.__data = self.dbManager.get_school_by_code(code)
        obj = self.search_class(code)
        return  obj


    # '根据班级代码，从班级数据库里边删除该班级的信息'
    # def delete_school(self, code):
    #     if code != '':
    #         if self.__data.get(code) != None:
    #             self.__data.pop(code)

    '输出全部班级的信息'
    def show_all_school(self):
        self.__data = self.dbManager.get_all_school()

        if len(self.__data) > 0:
            print("**********************************************************************")
            for key in self.__data:
                obj = self.__data[key]
                print("班级代码:{0}    |班级名称:{1}    |班级地址:{2}    ".format(obj.code, obj.name, obj.address))
            print("**********************************************************************")

        else:
            print("数据库里边还没有班级信息，请先添加班级信息到内存数据库！")


    '根据班级代码输出指定班级的信息'
    def show_school(self, code):
        self.__data = self.dbManager.get_school_by_code(code)
        obj = self.search_school(code)
        print("**************************************************************************")
        print("班级代码:{0}    |班级名称:{1}    |班级地址:{2}    ".format(obj.code, obj.name, obj.address))
        print("**************************************************************************")

    '根据班级代码删除指定的'
    def delete_school(self, code):
        # self.__data.pop(code)
        self.dbManager.delete_school(code)
        self.__data = self.dbManager.get_all_school()
        print("班级代码为：{0}的班级信息删除完毕！".format(code))


    '更改班级信息'
    def edit_school(self, code, obj):
        # self.__data[code] = obj
        self.dbManager.edit_school(obj)

    '判断班级数据库是否为空'
    def is_empty(self):
        if len(self.__data) > 0:
            return False
        else:
            return True

    '将班级信息保存到文件'
    def save_school_to_file(self):
        print("方法未实现")
        return
        fo = open("school.txt","a+",encoding='utf-8')
        for key in self.__data:
            obj = self.__data[key]
            code = obj.code
            name = obj.name
            address = obj.address
            class_amount = obj.class_amount
            fo.write(code + "," + name + "," + address + "," + str(class_amount) + "\n")
        fo.close()

    '从文件里读取班级数据'
    def import_from_file(self):
        print("方法未实现")
        return
        if os.path.exists("school.txt")==False:
            return False
        else:
            fo = open("school.txt", "r+", encoding='utf-8')
            lines = fo.readlines()
            # dic_School = {}
            for line in lines:
                listLine = line.split(',')
                code = listLine[0]
                name = listLine[1]
                address = listLine[2]
                class_amount = listLine[3]
                school = School.School()
                school.code = code
                school.name = name
                school.address = address
                school.class_amount = class_amount
                # dic_School.update({code:school})
                self.add_school(school)
            fo.close()
            return True







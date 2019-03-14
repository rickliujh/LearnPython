from pac_school import School
import os
from sqlalchemy.orm import sessionmaker
from pac_DB_Common import DB_Manager
class School_Manager(object):
    def __init__(self):
        self.__data = {}
        self.dbManager = DB_Manager.School_DB()

    '添加一所学校的信息到学校数据库里边'
    def add_school(self, school):
        if isinstance(school, School.School):
            # self.__data.update({school.code:school})
            self.dbManager.add_school(school)
            self.__data = self.dbManager.get_all_school()

    '对外返回整个学校信息的数据库'
    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    '查找是否已经存在相同学校代码的学校'
    def is_exist(self, code):
        if code != '':
            if len(self.dbManager.get_school_by_code(code)) > 0:
                result = True
            else:
                result = False
        else:
            result = False
        return result

    '根据学校代码查找学校信息'
    def search_school(self, code):
        if code != '':
            if self.__data.get(code) != None:
                return self.__data.get(code)

    def get_school_by_code(self, code):
        self.__data = self.dbManager.get_school_by_code(code)
        obj = self.search_school(code)
        return  obj


    # '根据学校代码，从学校数据库里边删除该学校的信息'
    # def delete_school(self, code):
    #     if code != '':
    #         if self.__data.get(code) != None:
    #             self.__data.pop(code)

    '输出全部学校的信息'
    def show_all_school(self):
        self.__data = self.dbManager.get_all_school()

        if len(self.__data) > 0:
            print("**********************************************************************")
            for key in self.__data:
                obj = self.__data[key]
                print("学校代码:{0}    |学校名称:{1}    |学校地址:{2}    ".format(obj.code, obj.name, obj.address))
            print("**********************************************************************")

        else:
            print("数据库里边还没有学校信息，请先添加学校信息到内存数据库！")


    '根据学校代码输出指定学校的信息'
    def show_school(self, code):
        self.__data = self.dbManager.get_school_by_code(code)
        obj = self.search_school(code)
        print("**************************************************************************")
        print("学校代码:{0}    |学校名称:{1}    |学校地址:{2}    ".format(obj.code, obj.name, obj.address))
        print("**************************************************************************")

    '根据学校代码删除指定的'
    def delete_school(self, code):
        # self.__data.pop(code)
        self.dbManager.delete_school(code)
        self.__data = self.dbManager.get_all_school()
        print("学校代码为：{0}的学校信息删除完毕！".format(code))


    '更改学校信息'
    def edit_school(self, code, obj):
        # self.__data[code] = obj
        self.dbManager.edit_school(obj)

    '判断学校数据库是否为空'
    def is_empty(self):
        if len(self.__data) > 0:
            return False
        else:
            return True

    '将学校信息保存到文件'
    def save_school_to_file(self):
        fo = open("school.txt","a+",encoding='utf-8')
        for key in self.__data:
            obj = self.__data[key]
            code = obj.code
            name = obj.name
            address = obj.address
            class_amount = obj.class_amount
            fo.write(code + "," + name + "," + address + "," + str(class_amount) + "\n")
        fo.close()

    '从文件里读取学校数据'
    def import_from_file(self):
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


    '添加班级到学校'
    def add_class_to_school(self, school_code,  obj_class):
        obj_school = self.search_school(school_code)
        obj_school.add_class(obj_class)



# -*- coding: UTF-8 -*-
from pac_DB_Common import DB_Manager
from pac_student import Student

class Student_Manager(object):
    def __init__(self):
        self.__data = {}
        self.dbManager = DB_Manager.Student_DB()

    '添加一个学生的信息到学生数据库里边'
    def add_student(self, student):
        if isinstance(student, Student.Student):
            # self.__data.update({student.code:student})
            self.dbManager.add_student(student)
            self.__data = self.dbManager.get_all_student()

    '对外返回整个学生信息的数据库'
    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    '查找是否已经存在相同学生代码的学生'
    def is_exist(self, code):
        if code != '':
            if len(self.dbManager.get_student_by_code(code)) > 0:
                result = True
            else:
                result = False
        else:
            result = False
        return result

    '根据学生代码查找学生信息'
    def search_student(self, code):
        if code != '':
            if self.__data.get(code) != None:
                return self.__data.get(code)

    def get_student_by_code(self, code):
        self.__data = self.dbManager.get_student_by_code(code)
        obj = self.search_student(code)
        return  obj


    # '根据学生代码，从学生数据库里边删除该学生的信息'
    # def delete_student(self, code):
    #     if code != '':
    #         if self.__data.get(code) != None:
    #             self.__data.pop(code)

    '输出全部学生的信息'
    def show_all_student(self):
        self.__data = self.dbManager.get_all_student()

        if len(self.__data) > 0:
            print("**********************************************************************")
            for key in self.__data:
                obj = self.__data[key]
                print("学生代码:{0}    |学生名称:{1}    |学生年龄:{2}    |学生性别:{3}    |班级代码:{4}    |学校代码:{5}"
                .format(obj.code, obj.name, obj.age, obj.sex, obj.class_code, obj.school_code))
            print("**********************************************************************")

        else:
            print("数据库里边还没有学生信息，请先添加学生信息到内存数据库！")


    '根据学生代码输出指定学生的信息'
    def show_student(self, code):
        self.__data = self.dbManager.get_student_by_code(code)
        obj = self.search_student(code)
        print("**************************************************************************")
        print("学生代码:{0}    |学生名称:{1}    |学生年龄:{2}    |学生性别:{3}    |班级代码:{4}    |学校代码:{5}"
                .format(obj.code, obj.name, obj.age, obj.sex, obj.class_code, obj.school_code))
        print("**************************************************************************")

    '根据学生代码删除指定的'
    def delete_student(self, code):
        # self.__data.pop(code)
        self.dbManager.delete_student(code)
        self.__data = self.dbManager.get_all_student()
        print("学生代码为：{0}的学生信息删除完毕！".format(code))


    '更改学生信息'
    def edit_student(self, code, obj):
        # self.__data[code] = obj
        self.dbManager.edit_student(obj)

    '判断学生数据库是否为空'
    def is_empty(self):
        if len(self.__data) > 0:
            return False
        else:
            return True
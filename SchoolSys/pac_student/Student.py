# -*- coding: UTF-8 -*-

class Student:
    __slots__ = ('code', 'name', 'age', 'sex', 'school_code',
                 'class_code', '__student_data')

    def __init__(self):
        self.__student_data = {}

    def add(self):
        input_code = input("请输入学生代码:")
        self.code = input_code
        input_name = input("请输入学生名称:")
        self.name = input_name
        input_age = input("请输入学生年龄:")
        self.age = input_age
        input_sex = input("请输入学生性别:")
        self.sex = input_sex
        input_class_code = input("请输入学生所在班级代码:")
        self.class_code = input_class_code
        input_school_code = input("请输入学生所在学校代码:")
        self.school_code = input_school_code

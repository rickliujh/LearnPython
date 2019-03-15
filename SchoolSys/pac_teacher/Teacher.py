# -*- coding: UTF-8 -*-

class Teacher:
    __slots__ = ('code', 'name','school_code', '__teacher_data')

    def __init__(self):
        self.__teacher_data = {}

    def add(self):
        input_code = input("请输入教师代码:")
        self.code = input_code
        input_name = input("请输入教师名称:")
        self.name = input_name
        input_school_code = input("请输入教师所在学校代码:")
        self.school_code = input_school_code
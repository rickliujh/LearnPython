#!/usr/bin/python
# -*- coding: UTF-8 -*-
class School:
    __slots__ = ('code', 'name', 'address', 'class_amount', '__class_data')

    def __init__(self):
        self.__class_data = {}
        self.class_amount = 0

    def add(self):
        input_code = input("请输入学校代码:")
        self.code = input_code
        input_name = input("请输入学校名称:")
        self.name = input_name
        input_address = input("请输入学校地址:")
        self.address = input_address


    '查找是否已经存在相同学校代码的学校'
    def is_exist(self, code):
        result = True
        if code != '':
            if self.__class_data.get(code) != None:
                result = True
            else:
                result = False
        else:
            result = False
        return result

    def edit_school(self, code, obj):
        self.__class_data[code] = obj






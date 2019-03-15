# -*- coding: UTF-8 -*-
class Class:
    __slots__ = ('code', 'name', 'address', 'student_amount', 'master',  'school_code',
                 '__dic_student', '__dic_teacher')

    def __init__(self):
        self.student_amount = 0
        self.master = ""
        self.__dic_student = {}
        self.__dic_teacher = {}

    def add_class(self):
        school_code = input("请输入班级所属学校代码：")
        class_code = input("请输入班级代码：")
        name = input("请输入班级名称：")
        address = input("请输入班级地址：")


    '向指定的学校添加指定的班级信息'
    def add_class(self, class_obj):
        if isinstance(class_obj, Class.Class):
            self.__class_data.update({class_obj.code:class_obj})
            self.class_amount = str(eval(self.class_amount) + 1)

    '删除指定的班级信息'
    def delete_class(self,code):
        self.__class_data.pop(code)
        self.class_amount = str(eval(self.class_amount) - 1)

    def show_all_class(self):
        if len(self.__class_data) > 0:
            print("**********************************************************************")
            for key in self.__class_data:
                obj = self.__class_data[key]
                print("班级代码:{0}    |班级名称:{1}    |班级地址:{2}    |班级学生数量：{3}|班主任：{4}".format(obj.code, obj.name,
                obj.address, obj.student_amount, obj.master))
                print("**********************************************************************")

        else:
            print("数据库里边还没有学校信息，请先添加学校信息到内存数据库！")

    '根据学校代码输出指定学校的信息'

    def show_class(self, code):
        obj = self.search_class(code)
        print("**********************************************************************************")
        print("班级代码:{0}    |班级名称:{1}    |班级地址:{2}    |班级学生数量：{3}|班主任：{4}".format(obj.code, obj.name, obj.address,
                                                                                 obj.student_amount, obj.master))
        print("**********************************************************************************")

    '查找是否已经存在相同学校代码的班级'
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

    '根据指定的班级代码查找班级信息'
    def search_class(self, code):
        if code != '':
            if self.__class_data.get(code) != None:
                return self.__class_data.get(code)



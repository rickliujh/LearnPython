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



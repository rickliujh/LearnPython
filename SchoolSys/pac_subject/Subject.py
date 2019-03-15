class Subject:
    __slots__ = ('code', 'name', '__subject_data')

    def __init__(self):
        self.__subject_data = {}

    def add(self):
        input_code = input("请输入课程代码:")
        self.code = input_code
        input_name = input("请输入课程名称:")
        self.name = input_name
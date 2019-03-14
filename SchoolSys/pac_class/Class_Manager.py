from pac_class import Class
class Class_Data(object):
    def __init__(self):
        self.__data = {}

    def add_class(self, obj):
        self.__data.update({obj.code:obj})
        if isinstance(obj, Class.Class):
            self.__data.update({obj.code:obj})

    def get_class_data(self):
        return self.__data




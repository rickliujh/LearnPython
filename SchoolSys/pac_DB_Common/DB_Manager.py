from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from pac_school import School
from pac_class import Class


class DB_Manager:
    __slots__ = ('__engine', '__session', 'school', 'lesson',
                 'classes', 'student', 'teacher', 'subject')

    def __init__(self):

        self.__engine = create_engine("mysql+pymysql://root:123456@localhost/edusys",
                                      encoding="utf-8", echo=False, max_overflow=5)
        Base = automap_base()
        Base.prepare(self.__engine, reflect=True)
        Base.classes.keys()
        self.school = Base.classes.school
        self.lesson = Base.classes.lesson
        self.classes = Base.classes.classes
        self.student = Base.classes.student
        self.teacher = Base.classes.teacher
        self.subject = Base.classes.subject
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def get_session(self):
        return self.__session


class School_DB(DB_Manager):

    def __init__(self):
        super().__init__()

    '向数据库添加一所学校'

    def add_school(self, objSchool):
        dbSchool = self.school(school_code=objSchool.code,
                               school_name=objSchool.name, school_addr=objSchool.address)
        self.get_session().add(dbSchool)
        self.get_session().commit()

    '从数据库获取全部学校信息'

    def get_all_school(self):
        school_result = self.get_session().query(self.school).all()
        _dicSchool = {}
        for obj in school_result:
            objSchool = School.School()
            objSchool.code = obj.school_code
            objSchool.name = obj.school_name
            objSchool.address = obj.school_addr
            _dicSchool.update({obj.school_code: objSchool})
        return _dicSchool

    '根据学校编码，从数据库获取指定的学校信息'

    def get_school_by_code(self, code):
        school_result = self.get_session().query(
            self.school).filter(self.school.school_code == code)
        _dicSchool = {}
        for obj in school_result:
            objSchool = School.School()
            objSchool.code = obj.school_code
            objSchool.name = obj.school_name
            objSchool.address = obj.school_addr
            _dicSchool.update({obj.school_code: objSchool})
        return _dicSchool

    '根据学校编码，从数据库删除指定的学校信息'

    def delete_school(self, code):
        self.get_session().query(self.school).filter(
            self.school.school_code == code).delete()
        self.get_session().commit()

    def edit_school(self, obj):
        attrs = {
            "school_name": obj.name,
            "school_addr": obj.address
        }
        self.get_session().query(self.school).filter(
            self.school.school_code == obj.code).update(attrs)
        self.get_session().commit()


class Class_DB(DB_Manager):

    def __init__(self):
        super().__init__()

    '向数据库添加一个班级'

    def add_class(self, objClass):
        dbClass = self.classes(class_code=objClass.code, class_name=objClass.name,
                               class_addr=objClass.address, school_code=objClass.school_code)
        self.get_session().add(dbClass)
        self.get_session().commit()

    '从数据库获取全部班级信息'

    def get_all_class(self):
        class_result = self.get_session().query(self.classes).all()
        _dicClass = {}
        for obj in class_result:
            objClass = Class.Class()
            objClass.code = obj.class_code
            objClass.name = obj.class_name
            objClass.address = obj.class_addr
            objClass.school_code = obj.school_code
            _dicClass.update({obj.class_code: objClass})
        return _dicClass

    '根据班级编码，从数据库获取指定的班级信息'

    def get_class_by_code(self, code):
        class_result = self.get_session().query(
            self.classes).filter(self.classes.class_code == code)
        _dicClass = {}
        for obj in class_result:
            objClass = Class.Class()
            objClass.code = obj.class_code
            objClass.name = obj.class_name
            objClass.address = obj.class_addr
            objClass.school_code = obj.school_code
            _dicClass.update({obj.class_code: objClass})
        return _dicClass

    '根据班级编码，从数据库删除指定的班级信息'

    def delete_class(self, code):
        self.get_session().query(self.classes).filter(
            self.classes.class_code == code).delete()
        self.get_session().commit()

    def edit_class(self, obj):
        attrs = {
            "class_name": obj.name,
            "class_addr": obj.address
        }
        self.get_session().query(self.classes).filter(
            self.classes.class_code == obj.code).update(attrs)
        self.get_session().commit()

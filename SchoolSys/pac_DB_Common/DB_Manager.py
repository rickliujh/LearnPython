from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from pac_school import School
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
            _dicSchool.update({obj.school_code:objSchool})
        return _dicSchool



    '根据学校编码，从数据库获取指定的学校信息'

    def get_school_by_code(self, code):
        school_result = self.get_session().query(self.school).filter(self.school.school_code == code)
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
        self.get_session().query(self.school).filter(self.school.school_code == code).delete()
        self.get_session().commit()

    def edit_school(self, obj):
        attrs = {
            "school_name":obj.name,
            "school_addr":obj.address
        }
        self.get_session().query(self.school).filter(self.school.school_code == obj.code).update(attrs)
        self.get_session().commit()

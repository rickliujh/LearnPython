# -*- coding: UTF-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from pac_school import School
from pac_class import Class
from pac_teacher import Teacher
from pac_student import Student
from pac_subject import Subject
from database import Settings


class DB_Manager:
    __slots__ = ('__engine', '__session', 'school', 'lesson',
                 'classes', 'student', 'teacher', 'subject')

    def __init__(self):
        DbConnection = "mysql+pymysql://{0}:{1}@{2}/{3}".format(
            Settings.DATABASE['username'],
            Settings.DATABASE['password'],
            Settings.DATABASE['host'],
            Settings.DATABASE['database'],
        )
        self.__engine = create_engine(
            DbConnection, encoding="utf-8", echo=False, max_overflow=5)
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


class Teacher_DB(DB_Manager):

    def __init__(self):
        super().__init__()

    '向数据库添加一个教师'

    def add_teacher(self, objTeacher):
        dbTeacher = self.teacher(teacher_code=objTeacher.code,
                                 teacher_name=objTeacher.name, school_code=objTeacher.school_code)
        self.get_session().add(dbTeacher)
        self.get_session().commit()

    '从数据库获取全部教师信息'

    def get_all_teacher(self):
        teacher_result = self.get_session().query(self.teacher).all()
        _dicTeacher = {}
        for obj in teacher_result:
            objTeacher = Teacher.Teacher()
            objTeacher.code = obj.teacher_code
            objTeacher.name = obj.teacher_name
            objTeacher.school_code = obj.school_code
            _dicTeacher.update({obj.teacher_code: objTeacher})
        return _dicTeacher

    '根据教师编码，从数据库获取指定的教师信息'

    def get_teacher_by_code(self, code):
        teacher_result = self.get_session().query(
            self.teacher).filter(self.teacher.teacher_code == code)
        _dicTeacher = {}
        for obj in teacher_result:
            objTeacher = Teacher.Teacher()
            objTeacher.code = obj.teacher_code
            objTeacher.name = obj.teacher_name
            objTeacher.school_code = obj.school_code
            _dicTeacher.update({obj.teacher_code: objTeacher})
        return _dicTeacher

    '根据教师编码，从数据库删除指定的教师信息'

    def delete_teacher(self, code):
        self.get_session().query(self.teacher).filter(
            self.teacher.teacher_code == code).delete()
        self.get_session().commit()

    def edit_teacher(self, obj):
        attrs = {
            "teacher_name": obj.name
        }
        self.get_session().query(self.teacher).filter(
            self.teacher.teacher_code == obj.code).update(attrs)
        self.get_session().commit()


class Student_DB(DB_Manager):

    def __init__(self):
        super().__init__()

    '向数据库添加一个学生'

    def add_student(self, objStudent):
        dbStudent = self.student(
            student_code=objStudent.code,
            student_name=objStudent.name,
            school_code=objStudent.school_code,
            class_code=objStudent.class_code,
            student_sex=objStudent.sex,
            student_age=objStudent.age
        )
        self.get_session().add(dbStudent)
        self.get_session().commit()

    '从数据库获取全部学生信息'

    def get_all_student(self):
        student_result = self.get_session().query(self.student).join(self.classes.id).join(self.school.id).all()
        _dicStudent = {}
        for obj in student_result:
            objStudent = Student.Student()
            objStudent.code = obj.student_code
            objStudent.name = obj.student_name
            objStudent.school_code = obj.school_code
            objStudent.class_code = obj.class_code
            objStudent.age = obj.student_age
            objStudent.sex = obj.student_sex
            _dicStudent.update({obj.student_code: objStudent})
        return _dicStudent

    '根据学生编码，从数据库获取指定的学生信息'

    def get_student_by_code(self, code):
        student_result = self.get_session().query(
            self.student).filter(self.student.student_code == code)
        _dicStudent = {}
        for obj in student_result:
            objStudent = Student.Student()
            objStudent.code = obj.student_code
            objStudent.name = obj.student_name
            objStudent.school_code = obj.school_code
            objStudent.class_code = obj.class_code
            objStudent.age = obj.student_age
            objStudent.sex = obj.student_sex
            _dicStudent.update({obj.student_code: objStudent})
        return _dicStudent

    '根据学生编码，从数据库删除指定的学生信息'

    def delete_student(self, code):
        self.get_session().query(self.student).filter(
            self.student.student_code == code).delete()
        self.get_session().commit()

    def edit_student(self, obj):
        attrs = {
            "student_name": obj.name,
            "student_age": obj.age,
            "student_sex": obj.sex,
            "class_code": obj.class_code,
            "school_code": obj.school_code
        }
        self.get_session().query(self.student).filter(
            self.student.student_code == obj.code).update(attrs)
        self.get_session().commit()


class Subject_DB(DB_Manager):

    def __init__(self):
        super().__init__()

    '向数据库添加一个课程'

    def add_subject(self, objSubject):
        dbSubject = self.subject(
            subject_code=objSubject.code,
            subject_name=objSubject.name,
        )
        self.get_session().add(dbSubject)
        self.get_session().commit()

    '从数据库获取全部课程信息'

    def get_all_subject(self):
        subject_result = self.get_session().query(self.subject).all()
        _dicSubject = {}
        for obj in subject_result:
            objSubject = Subject.Subject()
            objSubject.code = obj.subject_code
            objSubject.name = obj.subject_name
            _dicSubject.update({obj.subject_code: objSubject})
        return _dicSubject

    '根据课程编码，从数据库获取指定的课程信息'

    def get_subject_by_code(self, code):
        subject_result = self.get_session().query(
            self.subject).filter(self.subject.subject_code == code)
        _dicSubject = {}
        for obj in subject_result:
            objSubject = Subject.Subject()
            objSubject.code = obj.subject_code
            objSubject.name = obj.subject_name
            _dicSubject.update({obj.subject_code: objSubject})
        return _dicSubject

    '根据课程编码，从数据库删除指定的课程信息'

    def delete_subject(self, code):
        self.get_session().query(self.subject).filter(
            self.subject.subject_code == code).delete()
        self.get_session().commit()

    def edit_subject(self, obj):
        attrs = {
            "subject_name": obj.name
        }
        self.get_session().query(self.subject).filter(
            self.subject.subject_code == obj.code).update(attrs)
        self.get_session().commit()

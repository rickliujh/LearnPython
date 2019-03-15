import sys
sys.path.append("D:\Code\LearnPython\SchoolSys")
from pac_DB_Common.DB_Manager import Student_DB
from pac_DB_Common import DB_Manager
from pac_student import Student


dbManager = DB_Manager.Student_DB()
obj = Student.Student()


def case_add_student():
    obj.code = '2018010101'
    obj.name = "小红"
    obj.age = '21'
    obj.sex = '女'
    obj.school_code = '010'
    obj.class_code = '01001'
    dbManager.add_student(obj)
    return True


def case_get_all_student():
    studentList = dbManager.get_all_student()
    return studentList


def case_get_student_by_code():
    student_ = dbManager.get_student_by_code('2018010101')
    return student_


def case_edit_student():
    obj.name = "翠花"
    obj.age = '80'
    obj.sex = '未知'
    obj.school_code = '011'
    obj.class_code = '01002'
    dbManager.edit_student(obj)


def case_delete_student():
    dbManager.delete_student('2018010101')


if __name__ == "__main__":
    print("初始化测试环境")
    case_delete_student()
    print("---测试开始---")
    print("#打印现有学生")
    student = case_get_all_student()
    for i in student:
        print("名称 {0} 性别 {1} 年龄 {2} 代码 {3} 学校代码 {4} 班级代码 {5}".format(
            student[i].name, student[i].sex, student[i].age, student[i].code, student[i].school_code, student[i].class_code))
        pass
    print("#添加一个学生")
    case_add_student()
    print("名称 {0} 性别 {1} 年龄 {2} 代码 {3} 学校代码 {4} 班级代码 {5}".format(
            obj.name, obj.sex, obj.age, obj.code, obj.school_code, obj.class_code))
    print("#修改学生")
    case_edit_student()
    print("#检查是否修改成功")
    student_ = case_get_student_by_code()
    if student_['2018010101'].name == obj.name:
        print('#成功')
        pass
    else:
        print("#失败")
        pass
    print("#删除学生")
    case_delete_student()
    print("#检查是否删除成功")
    student_ = case_get_student_by_code()
    if len(student_) == 0:
        print("---测试成功---")
        pass
    else:
        print("---测试失败---")
        pass

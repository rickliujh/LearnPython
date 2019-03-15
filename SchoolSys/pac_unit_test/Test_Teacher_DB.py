import sys
sys.path.append("D:\Code\LearnPython\SchoolSys")

from pac_teacher import Teacher
from pac_DB_Common import DB_Manager
from pac_DB_Common.DB_Manager import Teacher_DB

dbManager = DB_Manager.Teacher_DB()
obj = Teacher.Teacher()

def case_add_teacher():
    obj.code = '01001'
    obj.name = "廖雪峰"
    obj.school_code = '010'
    dbManager.add_teacher(obj)
    return True

def case_get_all_teacher():
    teacherList = dbManager.get_all_teacher()
    return teacherList

def case_get_teacher_by_code():
    teacher_ = dbManager.get_teacher_by_code('01001')
    return teacher_

def case_edit_teacher():
    obj.name = "阮一峰"
    dbManager.edit_teacher(obj)

def case_delete_teacher():
    dbManager.delete_teacher('01001')

if __name__ == "__main__":
    print("初始化测试环境")
    case_delete_teacher()
    print("---测试开始---")
    print("#打印现有老师")
    teacheres = case_get_all_teacher()
    for i in teacheres:
        print("名称 {0} 代码 {1} 学校代码 {2}".format(teacheres[i].name,teacheres[i].code,teacheres[i].school_code))
        pass
    print("#添加一个老师")
    case_add_teacher()
    print("名称 {0} 代码 {1} 学校代码 {2}".format(obj.name,obj.code,obj.school_code))
    print("#修改老师")
    case_edit_teacher()
    print("#检查是否修改成功")
    teacher_ = case_get_teacher_by_code()
    if teacher_['01001'].name == obj.name:
        print('#成功')
        pass
    else:
        print("#失败")
        pass
    print("#删除老师")
    case_delete_teacher()
    print("#检查是否删除成功")
    teacher_ = case_get_teacher_by_code()
    if len(teacher_) == 0:
        print("---测试成功---")
        pass
    else:
        print("---测试失败---")
        pass


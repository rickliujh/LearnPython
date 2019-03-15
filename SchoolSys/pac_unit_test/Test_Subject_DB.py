import sys
sys.path.append("D:\Code\LearnPython\SchoolSys")

from pac_subject import Subject
from pac_DB_Common import DB_Manager
from pac_DB_Common.DB_Manager import Subject_DB

dbManager = DB_Manager.Subject_DB()
obj = Subject.Subject()

def case_add_subject():
    obj.code = '1001'
    obj.name = "python开发"
    dbManager.add_subject(obj)
    return True

def case_get_all_subject():
    subjectList = dbManager.get_all_subject()
    return subjectList

def case_get_subject_by_code():
    subject_ = dbManager.get_subject_by_code('1001')
    return subject_

def case_edit_subject():
    obj.name = "python网络编程"
    dbManager.edit_subject(obj)

def case_delete_subject():
    dbManager.delete_subject('1001')

if __name__ == "__main__":
    print("初始化测试环境")
    case_delete_subject()
    print("---测试开始---")
    print("#打印现有课程")
    subject = case_get_all_subject()
    for i in subject:
        print("名称 {0} 代码 {1}".format(subject[i].name,subject[i].code))
        pass
    print("#添加一个课程")
    case_add_subject()
    print("名称 {0} 代码 {1}".format(obj.name,obj.code))
    print("#修改课程")
    case_edit_subject()
    print("#检查是否修改成功")
    subject_ = case_get_subject_by_code()
    if subject_['1001'].name == obj.name:
        print('#成功')
        pass
    else:
        print("#失败")
        pass
    print("#删除课程")
    case_delete_subject()
    print("#检查是否删除成功")
    subject_ = case_get_subject_by_code()
    if len(subject_) == 0:
        print("---测试成功---")
        pass
    else:
        print("---测试失败---")
        pass


import sys
sys.path.append("D:\Code\LearnPython\SchoolSys")

from pac_class import Class
from pac_DB_Common import DB_Manager
from pac_DB_Common.DB_Manager import Class_DB

dbManager = DB_Manager.Class_DB()
obj = Class.Class()

def case_add_class():
    obj.code = '001'
    obj.address = "格物楼"
    obj.name = "软件工程一班"
    obj.school_code = '010'
    dbManager.add_class(obj)
    return True

def case_get_all_class():
    classList = dbManager.get_all_class()
    return classList

def case_get_class_by_code():
    class_ = dbManager.get_class_by_code('001')
    return class_

def case_edit_class():
    obj.name = "计算机科学与技术一班"
    obj.address = "致知楼"
    dbManager.edit_class(obj)

def case_delete_class():
    dbManager.delete_class('001')

if __name__ == "__main__":
    print("初始化测试环境")
    case_delete_class()
    print("---测试开始---")
    print("#打印现有班级")
    classes = case_get_all_class()
    for i in classes:
        print("名称 {0} 代码 {1} 地址 {2}".format(classes[i].name,classes[i].code,classes[i].address))
        pass
    print("#添加一个班级")
    case_add_class()
    print("名称 {0} 代码 {1} 地址 {2}".format(obj.name,obj.code,obj.address))
    print("#修改班级")
    case_edit_class()
    print("#检查是否修改成功")
    class_ = case_get_class_by_code()
    if class_['001'].name == obj.name:
        print('#成功')
        pass
    else:
        print("#失败")
        pass
    print("#删除班级")
    case_delete_class()
    print("#检查是否删除成功")
    class_ = case_get_class_by_code()
    if len(class_) == 0:
        print("---测试成功---")
        pass
    else:
        print("---测试失败---")
        pass


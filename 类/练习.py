#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
'''
角色：学校、学员、课程、讲师
要求
1、创建北京、上海2所学校
2、创建linux、python、go3个课程，linux\py在北京开，go在上海开
3、课程包括，周期、价格，通过学校创建课程
4、通过学校创建班级，班级关联课程、讲师
5、创建学员时，选择学校，关联班级
6、创建讲师角色时要关联学校
7、提供两个角色接口
7.1、学员视图，可以注册，交学费，选择班级
7.2、讲师可管理自己的班级，上课时学案则班级，查看学员列表，修改所管理的学员的成绩
7.3、管理视图，创建讲师，创建班级，创建课程
8、上面的操作产生的数据都通过公pickle序列化保存到文件里
'''


class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.course = []
        self.students = []
        self.teachers = []
        self.grade = []

    #def createGrade(self, grade):


class Grade(object):
    def __init__(self, grade):
        self.grade = grade
        self.course = []
        self.teachers = []
        self.students = []
class SchoolMember(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teachers(SchoolMember):
    pass
class Students(SchoolMember):
    pass

class Courses(object):
    def __init__(self, course_type, time, price):
        self.course_type = course_type
        self.price = price
        self.time = time

#创建学校
beijingSchool = School("北京分校", "北京")
shanghaiSchool = School("上海分校", "伤害")

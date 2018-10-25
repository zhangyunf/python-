#-*- coding:utf-8 -*-
#!Author:YunFei Zhang

class School(object):

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []
    def enroll(self, stu_obj):
        print("为学员%s办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        -------info of Teacher:%s-----
        name:%s
        age:%s
        sex:%s
        salary:%s
        course:%s''' % (self.name, self.age, self.sex, self.salary, self.course))
    def teach(self):
        print("%s isteaching course [%s]" % (self.name, self.course))

class Student(SchoolMember):

    def __init__(self, name, age, sex, stu_id, grade):
        super(Teacher, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
        -------info of Teacher:%s-----
        name:%s
        age:%s
        sex:%s
        stu_id:%s
        grade:%s''' % (self.name, self.age, self.sex, self.stu_id, self.grade))
    def pay_tuition(self, amount):
        print("%s has paid tution for $%s" % (self.name, amount))

school = School("一中", "好望角")
t1 = Teacher("张三", 56, "M", 20000, "linux")
s1 = Student("李四", 18, "M", 12, "大一")
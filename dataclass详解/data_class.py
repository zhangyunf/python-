#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import dataclasses
from dataclasses import field

@dataclasses.dataclass
class Student(object):
    name: str
    sex: str
    age: int
    score: float

    def description(self):
        print("name:{name} sex:{sex} age:{age} score:{score}".format(name=self.name, sex=self.sex, age=self.age, score=self.score))


@dataclasses.dataclass
class MyClass(object):
    """
    变量名称：变量类型
    注：此处的变量类型只是起表明作用，无约束作用。例如变量a，如果实例化中a=[1,2,3]。则实例中的a则为列表类型
    """
    # 定义类变量
    student: Student
    # 定义字符串
    className: str
    # 定义整数类型
    age: int
    # 定义浮点类型
    score: float
    # 定义列表类型
    teacher: list
    # 定义字典类型
    a: dict



if __name__ == '__main__':
    # 实例化
    studentOne = Student(name="张三", sex="男", age=15, score=90)
    myClass = MyClass(className="张三", age=18, score=90.9, teacher=[1, 2, 3], a={"a": "ff"}, student=studentOne)
    myClass.student.description()

    #

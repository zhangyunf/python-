# dataclass简介
```text
@dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
init:默认是True,将生成__init__()方法
repr:默认为True,将生成__repr__()方法。
eq:默认为True,将生成__eq__()方法。比较是否相等 ==
order:默认为False，为True时，将生成__lt__()、__le__()、__gt__()、__ge__()方法.
unsafe_hash:默认为False,为True时，
frozen:如为真值 (默认值为 False)，则对字段赋值将会产生异常。 这模拟了只读的冻结实例。 如果在类中定义了 __setattr__() 或 __delattr__() 则将会引发 TypeError。
```
```python
import dataclasses


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
```
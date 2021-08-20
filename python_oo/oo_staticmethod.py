# 静态方法
"""
概念：类的工具包，不跟类绑定，也不跟具体的实例绑定，做一些跟类和跟实例没关系的事，不能访问类属性也不能访问实例属性

"""


class Chinese:
    """中国人的类"""
    age = 22
    sex = 'male'

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    @staticmethod
    def Features():
        print('会走,会跑,会吃,会睡觉')


people = Chinese('tom', 1.65, 62)
print(people.__dict__)
Chinese.Features()      # 静态方法提倡用类名去访问
print(Chinese.__dict__)

# 给类添加静态方法


@staticmethod
def staticMethod():
    print("我是后面添加的静态方法")


Chinese.func = staticMethod
people.func()

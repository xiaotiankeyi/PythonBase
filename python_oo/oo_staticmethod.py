# 静态方法
"""
概念:类的工具包,不跟类绑定,也不跟具体的实例绑定,做一些跟类和跟实例没关系的事,不能访问类属性也不能访问实例属性
1、类方法和静态方法都是通过函数装饰器@staticmethod的方式实现的,静态方法无需传入self参数或者是cls参数（但不等同于不能传入参数）
2、静态方法有点像附属于类对象的“工具”,与普通函数不同,调用静态方法时,只能通过类对象（或者实例对象）
    而不能脱离类对象使用,即静态方法被‘束缚’在类对象中
"""


class Chinese:
    """中国人的类"""
    age = 22
    sex = 'male'

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def output(self):
        """class中的实例方法调用静态方法"""
        self.Features(val='体重'+ str(self.weight))

    @staticmethod
    def Features(val):
        print('会走,会跑,会吃,会睡觉', val)


people = Chinese('tom', 1.65, 62)
people.Features("实例对象也是支持调用静态方法的")
people.output()
print(people.__dict__)

Chinese.Features("可以专递参数")  # 静态方法提倡用类名去访问
print(Chinese.__dict__)


# 在外部给类对象添加一个静态方法


# 首先先定义好静态方法
@staticmethod
def staticMethod():
    print("我是后面添加的静态方法")


# 把定义好的静态方法关联到类对象
Chinese.func = staticMethod
Chinese.func()

# 类方法
"""
类方法概念：
    1、class在调用自己的函数属性时,需要和实例捆绑在一起，类方法就是不通过实例来捆绑，
    就只执行类的数据属性和类的函数属性就是类方法，就是类本身调用自身的数据及函数属性，跟实例没有任何关系,
"""


class People:
    """类说明定义一个中国人的类"""
    area = 9600000

    def __init__(self, name, age, sex, height, weight):
        self.user = name
        self.height = height
        self.weight = weight
        self.sex = sex
        self.age = age

    def Features(self):
        # return '%s会走,会跑,会吃,会睡觉' % self.user
        print('%s是个人他会走,会跑,会吃,会睡觉' % self.user)

    def borrow(self):
        print('该函数属性需要获取class数据属性的值时，必须通过对(实例)对象来完成对数据属性的调用%s' % People.area)

    @classmethod  # 给类用的
    def seek(cls):
        print('调用类的函数属性,不通过对象来捆绑调用%s' % cls.area)


r = People('tom', 22, '男', '165cm', '60kg')

People.seek()       # 调用自身类方法时不需要绑定实例对象
People.borrow(r)    # 调用方法时需要绑定实例对象

print(r.area)
r.seek()

# 增加一个类方法


@classmethod
def classMethod(cls):
    print('我是类方法，我调用了%s' % cls.area)


People.func = classMethod
r.func()

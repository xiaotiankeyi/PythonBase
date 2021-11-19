# 类方法
"""
类方法概念：
    1、class在调用自己的函数属性时,需要和实例捆绑在一起，类方法就是不通过实例来捆绑，
    2、就只执行类的数据属性和类的函数属性就是类方法，就是类本身调用自身的数据及函数属性，跟实例没有任何关系,
    类方法需要传入cls参数
"""


class People:
    """类说明定义一个中国人的类"""
    area = 9600000
    value = 44323

    def __init__(self, name, age, sex, height, weight):
        self.user = name
        self.height = height
        self.weight = weight
        self.sex = sex
        self.age = age

    def Features(self):
        # return '%s会走,会跑,会吃,会睡觉' % self.user
        print('%s是个人他会走,会跑,会吃,会睡觉' % self.user, self.area)

    def borrow(self):
        print('该函数属性需要获取class数据属性的值时，必须通过对(实例)对象来完成对数据属性的调用%s' % People.area)

    @classmethod  # 给类用的
    def seek(cls):
        print('调用类的函数属性,不通过对象来捆绑调用%s' % cls.area)

    @classmethod
    def modify(cls):
        """类方法调用类方法"""
        cls.seek()


r = People('tom', 22, '男', '165cm', '60kg')

People.seek()       # 类对象调用自身类方法时不需要绑定实例对象
People.borrow(r)    # 类对象调用实例方法时需要绑定实例对象

print(r.area)       # 实例对象可以调用类的数据属性
r.seek()        # 实例对象也可以调用类方法
r.modify()

# 增加一个类方法


@classmethod
def classMethod(cls):
    print('我是类方法，我调用了%s' % cls.value)


People.func = classMethod
People.func()

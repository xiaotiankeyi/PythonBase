# 静态属性@property

"""
    概念：静态属性其实就是数据属性，把class的函数属性封装成数据属性的形式，在外部调用的时候感受不到运行逻辑
    作用及实例操作：1.可以访问到实例(对象)自身的数据属性,也可以访问类的数据属性及函数属性
                 2.与所定义的属性配合getter/setter使用，这样可以防止属性被修改。
"""


class PePole(object):
    """类说明定义一个中国人的类"""

    status = '状态'

    def __init__(self, name, age, sex, height, weight):
        self.user = name
        self.height = height
        self.weight = weight
        self.sex = sex
        self.__age = age

    def Features(self):
        # return '%s会走,会跑,会吃,会睡觉' % self.user
        return '%s是个人他会走,会跑,会吃,会睡觉' % self.user

    @property       # 这里只是简单的实现掉用时不用加()
    def trait(self):
        return "{}的性别是{}".format(self.user, self.sex)

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def set_Age(self, value):
        """进行实例属性修改时做判断"""
        if not isinstance(value, int):
            """判断传入的参数是不是int类型"""
            raise ValueError('score must be an integer!')
        if 0 < value < 100:
            self.__age = value
        else:
            print('修改失败。。。。score must between 0 ~ 100!')

    @property
    def count(self):
        return "{} 的身高体重指数为 {:.2f}% ".format(
            self.user, (self.weight / (self.height * self.height)))


people_1 = PePole('jack', 2222, '男', 1.65, 62)

print(people_1.Features())  # 对象访问方法
print(people_1.trait)   # 加了@property后，可以用调用属性的形式来调用方法,后面不需要加()

print(people_1.get_age)
people_1.set_Age = 33       # 当对其修改时会做判断处理了
print(people_1.get_age)

print(people_1.count)
print(people_1.weight)
print('===========================================')

# print(PePole.Features(people_1))  # 类访问
# print(PePole.status)

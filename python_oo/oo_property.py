# 静态属性
"""
    概念：静态属性其实就是数据属性，把class的函数属性封装成数据属性的形式，在外部调用的时候感受不到运行逻辑
    作用及实例操作：可以访问到实例(对象)自身的数据属性,也可以访问类的数据属性及函数属性

"""


class Pepole:
    """类说明定义一个中国人的类"""

    status = '状态'

    # ==========起始位置,初始化
    def __init__(self, name, age, sex, height, weight):
        self.user = name
        self.height = height
        self.weight = weight
        self.sex = sex
        self.age = age

    def Features(self):
        # return '%s会走,会跑,会吃,会睡觉' % self.user
        return '%s是个人他会走,会跑,会吃,会睡觉' % self.user

    @property
    def trait(self):
        return "{}的性别是{}".format(self.user, self.sex)

    @property
    def posture(self):
        return "{}的体重是{}kg,身高是{}m,年龄是{}".format(self.user, self.weight, self.height, self.age)

    @property
    def count(self):
        return "{} 的身高体重指数为 {:.2f}% ".format(self.user, (self.weight / (self.height * self.height)))

    pass


people = Pepole('tom', 22, '男', '165cm', '60kg')

people_1 = Pepole('jack', 22, '男', 1.65, 62)
print(people_1.__dict__)
print(people_1.Features())  # 对象访问
print(people_1.trait)
print(people_1.posture)     #优势>>在调用函数属性是不需要添加小括号
print(people_1.count)
print(people_1.weight)
print('===========================================')

print(Pepole.Features(people))  # 类访问
print(Pepole.status)

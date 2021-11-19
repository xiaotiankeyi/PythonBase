# 静态属性@property

"""
    概念：静态属性其实就是数据属性，把class的函数属性封装成数据属性的形式，在外部调用的时候感受不到运行逻辑
    作用及实例操作：1.可以访问到实例(对象)自身的数据属性,也可以访问类的数据属性及函数属性
                 2.与所定义的属性配合getter/setter使用，这样可以防止属性被修改。
    我们可以使用@property装饰器来创建只读属性，@property装饰器会将方法转换为相同名称的只读属性,
    可以与所定义的属性配合使用，这样可以防止属性被修改。
    Property对象有三个方法，getter(), setter()和delete()，
"""


class PePole(object):
    """通过@property装饰器，实现对_age实例属性的约束，使其智能输入大于0小于100的数"""

    def __init__(self, name, age, sex, height, weight):
        self.user = name
        self.height = height
        self.weight = weight
        self.sex = sex
        self._age = age

    def Features(self):
        # return '%s会走,会跑,会吃,会睡觉' % self.user
        return '%s是个人他会走,会跑,会吃,会睡觉' % self.user

    @property  # 这里只是简单的实现掉用时不用加()
    def trait(self):
        return "{}的性别是{}".format(self.user, self.sex)

    @property
    def get_age(self):
        """转化为只读属性"""
        return self._age

    @get_age.setter
    def set_age(self, value):
        """对年龄实例属性修改时做判断实现了对年龄的扩展"""
        if not isinstance(value, int):
            """判断传入的参数是不是int类型"""
            raise ValueError('score must be an integer!')
        if 0 < value < 100:
            self._age = value
            print('修改成功！！')
        else:
            print('修改失败。。。。score must between 0 ~ 100!')


people = PePole('jack', 22222, '男', 1.65, 62)

print(people.__dict__)
print(people.Features())  # 实例对象访问实例方法
print(people.trait)  # 加了@property后，可以像调用属性的形式来调用方法,后面不需要加()

print(people.user)
print('该方法转化的为静态属性,只读：', people.get_age)
people.set_age = 33  # 当对其修改时会做判断处理了
print('修改后在查看：', people.get_age)


class Celsius:
    """该方法实现创建对象时就对值进行约束和在修改实例树形时对值进行约束"""
    def __init__(self, temperature=0, age=0):
        self.temperature = temperature
        self.age = age

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)

obj = Celsius(322)
print(obj.temperature)
print(obj.to_fahrenheit())

obj.temperature = 33
print(obj.temperature)

# 继承单继承和·多继承
"""
    python三大特性:继承\\多态\\封装
    概念:
        1、单继承、多继承
        2、子类可以继承父类的实例属性和实例方法及数据属性
        3、当子类中的数据属性和父类出现重名时,在调用时先在自身寻找
        4、两个概念 派生\\继承
    使用场景:当类之间有很多相同的功能,提取这些公共的功能做成基类,用继承较好
"""


class Chinese:
    """中国人的类"""
    height = "165cm"
    weight = "56kg"
    area = "960万"

    def Features(self):
        return '他所在的这个国家的面积是%s' % self.area


class Countries(Chinese):
    height = "180cm"

    def __init__(self, name, state):
        self.name = name
        self.state = state

    def update(self):
        return '%s所在的国家是%s,他的身高是%s,体重为%s,' % (
            self.name, self.state, self.height, self.weight)

    def alter(self):
        """和父类的数据属性出现重名命的值,优先调用自身的值"""
        print(self.height)


print(issubclass(Countries, Chinese))  # 判断是否是子类

accept = Countries('jack', 'chinese')
print(accept.alter())


# print(accept.update(), accept.Features())
# print(accept.Features())
# print(accept.height)      #通过子类生成的对象去访问父类的数据属性,,,,
# print(accept.area)


class Animal(object):

    def eat(self):
        # print("%s 吃 " %self.name)
        return '会吃'

    def drink(self):
        # print ("%s 喝 " %self.name)
        return '会喝'

    def shit(self):
        # print ("%s 拉 " %self.name)
        return '会叫'

    def pee(self):
        # print ("%s 撒 " %self.name)
        return '会撒'


class Feature(object):

    def running(self):
        return "会跑"

    def fight(self):
        return "会打"



# 多继承
class Cat(Animal, Feature):

    def __init__(self, name):
        self.name = name
        self.breed = '猫'

    def cry(self):
        # print('喵喵叫')
        return '会喵喵叫'


obj = Cat('波斯猫')

print(
    obj.name, '\n', '\t',
    obj.eat(), '\n', '\t',
    obj.drink(), '\n', '\t',
    obj.shit(), '\n', '\t',
    obj.pee(), '\n', '\t',
    obj.cry(), '\n', '\t',
    obj.running(), '\n', '\t'
)

print(isinstance(obj, Cat))  # 判断obj是不是Cat实例化而来的

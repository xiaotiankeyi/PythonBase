# 继承
"""
    python三大特性：继承\多态\封装
    概念：
        1、单继承、多继承
        2、子类可以继承父类的函数属性及数据属性
        3、当子类中的数据属性和父类出现重名时,在调用时先在自身寻找
        4、两个概念 派生\继承
    使用场景：当类之间有很多相同的功能，提取这些公共的功能做成基类，用继承较好
"""


class Chinese:
    """中国人的类"""
    height = "165cm"
    weight = "56kg"
    area = "960万"

    def Features(self):
        return '他所在的这个国家的面积是%s' % self.area


class Countries(Chinese):

    def __init__(self, name, state):
        self.name = name
        self.state = state

    def update(self):
        return '%s所在的国家是%s，他的身高是%s,体重为%s,' % (self.name, self.state,self.height, self.weight)

print(issubclass(Countries, Chinese))   #判断是否是子类

accept = Countries('jack', 'chinese')
# print(accept.update(), accept.Features())
# print(accept.Features())
# print(accept.height)      #通过子类生成的对象去访问父类的数据属性。。。。
# print(accept.area)


class Animal:

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

class Cat(Animal):

    def __init__(self, name):
        self.name = name
        self.breed = '猫'

    def cry(self):
        # print('喵喵叫')
        return '会喵喵叫'

object = Cat('波斯猫')

print(
    object.name,'\n','\t',
    object.eat(),'\n','\t',
    object.drink(),'\n','\t',
    object.shit(),'\n','\t',
    object.pee(),'\n','\t',
    object.cry()
)

print(isinstance(object, Cat))      #判断object是不是Cat实例化而来的

"""
1、数据属性 -----属于class的属性，也属于"类对象"的属性
2、函数属性 ---- 属于class的属性，"实例对象"可以调用类的函数属性
"""
import types

class Chinese(object):
    """中国人的类"""
    height = "165cm"
    weight = "56kg"

    def __init__(self, name):
        self.name = name

    def Features(self):
        print('会走,会跑,会吃,会睡觉')


people = Chinese("jack")  # 实例化一个对象

# 类数据属性增删改查操作
def Edit():
    Chinese.name = "jack"  # 增
    print(Chinese.__dict__)

    Chinese.weight = '60kg'  # 改
    print(Chinese.__dict__)

    del Chinese.height  # 删
    print(Chinese.__dict__)


Edit()


def like(self, foods):  # 先定义一个方法,并且调用新增加的数据属性
    print('>>>>>>>%s喜欢吃%s' % (self.name, foods))

# 为实例对象增加方法，只属于对象所有people
people.like = types.MethodType(like, people)
people.like("苹果")

# 为整个类增加一个函数方法
Chinese.func = like  # 增加这个方法
# print(Chinese.__dict__)
people.func('苹果')  # 调用这个方法


"""查看类的属性的一些方法,以及返回属性字典"""
print(dir(Chinese))
print(Chinese.__dict__)
print(Chinese.__dict__["weight"])
Chinese.__dict__["Features"](people)       # 类对象执行实例方法

print('==============查看类的特殊属性===============')
print(Chinese.__name__)  # 类名
print(Chinese.__doc__)  # 类说明,文档
print(Chinese.__module__)  # 显示当前所在模块
print(Chinese.__class__)

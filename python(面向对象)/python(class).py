"""
1、数据属性 -----属于class的属性，也属于实例(对象)的属性
2、函数属性 ---- 属于class的属性，实例(对象)可以调用类的函数属性
"""


class Chinese:
    """中国人的类"""
    height = "165cm"
    weight = "56kg"

    def Features(self):
        print('会走,会跑,会吃,会睡觉')


people = Chinese()  # 实例化一个对象

"""类数据属性增删改查操作"""


def group():
    Chinese.name = "jack"  # 增
    print(Chinese.__dict__)

    Chinese.weight = '60kg'  # 改
    print(Chinese.__dict__)

    del Chinese.height  # 删
    print(Chinese.__dict__)


# group()

"""类增加函数属性"""


def function():
    def like(self, foods):  # 先定义一个方法,并且调用新增加的数据属性
        print('>>>>>>>%s喜欢吃%s' % (self.name, foods))

    Chinese.func = like  # 增加这个方法
    print(Chinese.__dict__)

    people.func('苹果')  # 调用这个方法


# function()

"""查看类的属性的一些方法,以及返回属性字典"""
# print(dir(Chinese))
# print(Chinese.__dict__)
print(Chinese.__dict__["height"])
Chinese.__dict__["Features"](people)

print('==============查看类的特殊属性===============')
print(Chinese.__name__)  # 类名
print(Chinese.__doc__)  # 类说明,文档
print(Chinese.__module__)  # 显示当前所在模块

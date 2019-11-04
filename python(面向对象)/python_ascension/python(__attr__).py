"""
    概念：
        1、python内置的方法
        2、在不自己设定的时候，python就执行默认的设定
"""

class Chinese:
    """中国人的类"""
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def Features(self):
        print('会走,会跑,会吃,会睡觉')

    def __getattr__(self, item):
        return '没有找到%s相应的属性,就触发' % item

    def __setattr__(self, key, value):      #设定属性
        pass

people = Chinese(1.65, 62)      #触发setattr
# print(people.height)

print(people.name)      #触发getattr
print(people.sdoad)


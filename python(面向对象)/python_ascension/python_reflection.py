"""
    概念;
        1、反射底层操作就是操作__dict__
"""


class Chinese:
    """中国人的类"""

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def Features(self):
        return '会走,会跑,会吃,会睡觉'

    def __setattr__(self, key, value):  # 自定义setattr
        if type(value) is str or type(value) is int:
            self.__dict__[key] = value
            print('调用了自定义的__setattr__,设置成功')
        else:
            print('调用了自定义的__setattr__,必须是字符串或是数字')

    def __getattr__(self, item):  # 自定义getattr
        return '调用了自定义的__getattr__,没有找到%s方法或属性' % item

    def __delattr__(self, item):  # 自定义delattr
        if item == "name" or item == "height" or item == "weight":

            return "调用了自定义的__delattr__,不让删除"
        else:
            del self.__dict__[item]


if __name__ == "__main__":

    people = Chinese("1.65m", 62)
    print(people.__dict__)

    """判断对象people是否有相应的属性"""  # 同样适用于类
    print(hasattr(people, 'height'))
    print(hasattr(people, 'Features'))

    """判断二"""
    # print(getattr(people, 'height'))
    print(getattr(people, 'Features1',))  # 检查函数方法，有就返回函数地址，没找到就返回

    """为实例添加数据属性或是修改属性"""
    setattr(people, 'name', 45)  # 也可以添加函数属性
    setattr(people, 'age', 45.45)
    print(people.__dict__)

    """删除数据属性操作"""
    print(delattr(people, 'name'))
    print(people.__dict__)

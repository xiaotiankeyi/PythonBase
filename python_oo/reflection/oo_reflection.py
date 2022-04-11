# 反射,与及对字典的操作
# 概念:1、反射底层操作就是操作__dict__
# 自定义__setattr__现实对传入参数的验证
# 反射就是对hasattr和getattr的应用
# 注意,hasattr的应用,查找不存在的函数本来返回false,但是如果自定义了__getattr__就不报错,结果返回了true


class Chinese:
    """中国人的类"""

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def Features(self):
        return '会走,会跑,会吃,会睡觉'

    def __setattr__(self, key, value):  # 自定义setattr,但是没有对特定的实例属性做判断
        if isinstance(value, str) or isinstance(value, int):
            """判断是不是传入的value值是不是str或是int类型"""
            self.__dict__[key] = value
            print('调用了自定义的__setattr__,设置成功', key, value)
        else:
            print('调用了自定义的__setattr__,必须是字符串或是数字', key, value)


    def __getattr__(self, item):  # 自定义getattr
        return '调用了自定义的__getattr__,没有找到%s方法或属性' % item

    def __delattr__(self, item):  # 自定义delattr
        if item == "name" or item == "height" or item == "weight":
            # print("调用了自定义的__delattr__,不让删除")
            return "调用了自定义的__delattr__,不让删除"
        else:
            del self.__dict__[item]
            return '删除成功！！！'


if __name__ == "__main__":
    people = Chinese("1.65m", 62)
    print(people.__dict__)

    # hasattr判断对象people是否有相应的实例属性或是函数属性,有就返回true  # 同样适用于类
    print(hasattr(people, 'height'))
    print(hasattr(people, 'Features'))

    # getattr判断对象people是否有相应的实例属性或是函数属性,有就返回value,或是返回函数地址
    print(getattr(people, 'height'))        # 有就返回value
    print(getattr(people, 'Features1', ))  # 检查函数方法,有就返回函数地址,没找到就返回错误

    # 为实例对象添加实例属性或是修改属性
    setattr(people, 'name', 'jack')
    setattr(people, 'age', 23)
    print(people.__dict__)

    """删除数据属性操作"""
    # delattr(people, 'age')
    print(delattr(people, 'age'))
    print(people.__dict__)

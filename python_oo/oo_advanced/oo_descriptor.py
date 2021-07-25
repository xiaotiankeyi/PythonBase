# 描述符应用
""" 数据描述符的运用
    概念：数据描述符的组成包含
            def __get__(self)
            def __set__(self)
            def __del__(self)
    非数据描述符的组成
            def __get__(self),def __set__(self)中的一个加上def __del__(self)......
"""


# 运用描述符的方法对class所传参数做type判断
class Type():
    def __init__(self, key, Expect_type):
        self.key = key
        self.Expect_type = Expect_type

    def __get__(self, instance, owner):
        print("get方法")
        # print(instance)
        # print(owner)
        return instance.__dict__[self.key]
        pass

    def __set__(self, instance, value):
        print("set方法")
        # print(instance)
        # print(value)
        if isinstance(value, self.Expect_type):
            instance.__dict__[self.key] = value
        else:
            raise TypeError("%s只允许输入%s" % (self.key, self.Expect_type))
        pass

    def __delete__(self, instance):
        print("delete方法")
        # print(instance)
        instance.__dict__.pop(self.key)
        pass


class People():
    name = Type("name", str)
    age = Type("age", int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


human = People("jack", 22)  # 赋值触发set的方法
print(human.__dict__)

print("=======================" * 5)

print(human.name)  # 调用时触发get的方法

print("=======================" * 5)

print(human.__dict__)
human.name = 'Tom'  # 修改触发set方法
print(human.__dict__)

print("=======================" * 5)

print(human.__dict__)
del human.name  # 删除触发delete方法
print(human.__dict__)

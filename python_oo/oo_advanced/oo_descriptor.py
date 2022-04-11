# 描述符应用,实现对传入参数的验证！！！！

""" 数据描述符的运用
    概念:数据描述符的组成包含
            def __get__(self)  调用属性触发
            def __set__(self)   为属性赋值时触发
            def __del__(self)   删除属性时触发
    非数据描述符的组成
            def __get__(self),def __set__(self)中的一个加上def __del__(self)......
"""


# 运用描述符的方法对class所传参数做type判断
class Type(object):

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
        print(value)
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


class People(object):
    name = Type("name", str)
    age = Type("age", int)

    def __init__(self, name, age):
        self.name = name        # name和age被代理
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

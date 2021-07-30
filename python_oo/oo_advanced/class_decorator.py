# 类的装饰器
"""使用类的装饰器功能与描述符项结合来为class所传参数做判断"""


# 描述符
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


# 装饰器
def deco(**kwargs):
    def wrapper(obj):
        for key, val in kwargs.items():
            setattr(obj, key, Type(key, val))
        return obj

    return wrapper


@deco(name=str, age=int, height=int)
class people():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


print(people.__dict__)
user = people("jack", 22, 165)
print(user.__dict__)

# 单例模式

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "A"):
            A = super().__new__(cls, *args, **kwargs)
            cls.A = A

        return cls.A


class mycalss(Singleton):
    pass


c1 = mycalss()
c2 = mycalss()
print(id(c1))
print(id(c2))


class Singleton(object):

    def __init__(self):
        print("__init__")

    def __new__(cls, *args, **kwargs):
        print("__new__")
        if not hasattr(Singleton, "_instance"):
            print(" 创建新实例 ")
            Singleton._instance = object.__new__(cls)


a = Singleton()
b = Singleton()
print(id(a))
print(id(b))

# 自定义__doc__,返回对象的描述信息

class Foo(object):
    pass

    def __str__(self):  # 可以自定义修改return
        return '可以自定义修改return对象描述信息'

    def __repr__(self):
        return '在打印类的时候，控制类的输入......'


if __name__ == "__main__":
    obj = Foo()

    print(dir(Foo))
    print(Foo.__dict__)
    print('获取对象描述信息:', obj)
    print(obj.__repr__)

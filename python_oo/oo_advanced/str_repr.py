# 自定义__doc__,返回对象的描述信息

class Foo(object):

    def __str__(self):  # 可以自定义修改return
        # objList = [obj, obj1]打印的是地质
        return '可以自定义修改return对象描述信息'

    def __repr__(self):
        # objList = [obj, obj1]打印的是return值
        return f'在打印类的时候，控制类的输出......'


if __name__ == "__main__":
    obj = Foo()
    obj1 = Foo()
    objList = [obj, obj1]

    print(objList)
    print(dir(Foo))
    print(Foo.__dict__)
    print('获取对象描述信息:', obj)
    print(obj.__repr__)

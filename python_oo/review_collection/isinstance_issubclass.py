"""isinstance(obj,cls)_issubclass(sub,supe)"""


class Foo():
    pass


obj = Foo()

v = isinstance(obj, Foo)  # isinstance(obj, Foo)检查obj是否是类Foo的对象
print(v)


class Foo():
    pass


class create(Foo):
    pass


# issubclass(create,Foo)检查create是否是Foo的派生类或是crate是否继承了Foo类
f = issubclass(create, Foo)
print(f)

# isinstance(obj,cls)
# issubclass(sub,supe)"""


class Foo(object):
    pass


obj = Foo()

v = isinstance(obj, Foo)  # isinstance(obj, Foo)检查obj是否是类Foo的对象
print(v)


class Foo(object):
    pass


class Create(Foo):
    pass


f = issubclass(Create, Foo)     # 检查create是否是Foo的派生类或是crate是否继承了Foo类
print(f)

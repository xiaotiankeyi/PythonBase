
class Foo():
    "省内存的作用，尽量少用"
    # __slots__ = 'name'  #单个
    __slots__ = ['age', 'sex']  #多个

quest = Foo()
print(quest.__slots__)

print("文档说明>>>>>",Foo.__doc__)

print("来自于那个模块>>>>>", quest.__module__)
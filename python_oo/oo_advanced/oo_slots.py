# 当一个类需要创建大量实例时，可以通过__slots__声明实例所需要的属性

class Foo():
    # __slots__ = 'name'  #单个
    __slots__ = ['age', 'sex']  # 多个


quest = Foo()
print(quest.__slots__)

quest.age = 45
quest.sex = 'man'

print(quest.age)
print(quest.sex)

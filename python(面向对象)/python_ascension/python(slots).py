class Foo():
    # __slots__ = 'name'  #单个
    __slots__ = ['age', 'sex']  #多个

quest = Foo()
print(quest.__slots__)

quest.age = 45
quest.sex = 'man'

print(quest.age)
print(quest.sex)
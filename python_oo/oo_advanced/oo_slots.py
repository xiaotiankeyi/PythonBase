# 当一个类需要创建大量实例时,可以通过__slots__声明实例所需要的属性
# slots可以对动态添加实例属性和实例方法做限制
# 对类属性,静态方法,类方法的添加没有限制

class Foo(object):
    # __slots__ = 'name'  # 单个
    __slots__ = ['age', 'sex']  # 多个

    def __init__(self, age, sex):
        self.sex = sex
        self.age = age


obj = Foo(22, ' 男')
print(obj.__slots__)

obj.age = 45
obj.sex = 'man'
print(obj.age)
print(obj.sex)

# obj.addr = "北京"     # 被slots限制动态添加

Foo.birthday = "1997/01/23"     # 动态添加类属性没做限制
print(Foo.birthday)             

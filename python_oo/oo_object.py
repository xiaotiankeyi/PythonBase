# __init__实例属性
"""初始化构建函数"""


class PePole(object):
    """类说明定义一个中国人的类"""
    status = '特征'

    def __init__(self, name, age, sex, height, weight):
        self.user = name
        self.height = height
        self.weight = weight
        self.sex = sex
        self.age = age

    def Features(self):
        # return '%s会走,会跑,会吃,会睡觉' % self.user
        print('%s的%s是他是个人，他会走,会跑,会吃,会睡觉' % (self.user, self.status,))

    def trait(self):
        print("{}的性别是{}".format(self.user, self.sex))

    def posture(self):
        print(
            "{}的体重是{},身高是{},年龄是{}".format(
                self.user,
                self.weight,
                self.height,
                self.age))


people = PePole('tom', 22, '男', '165cm', '60kg')  # 实例化过程,self就是PePole,实例只有数据属性

print(people.__dict__)  # 查看实例属性
print(people.height)  # 调用实例属性,查看该属性的值
PePole.Features(people)  # class调用函数属性需要绑定实例对象
PePole.trait(people)  # class调用函数属性


def handle():  # 对象(实例)调用函数属性的正确方式
    people.Features()
    people.trait()
    people.posture()


handle()

"""实例属性的增删改查"""
print(people.height)  # 调用数据属性,查看该属性的值

people.addr = '北京'  # 增加一个实例属性
print(people.__dict__)

setattr(people, 'birthday', '2021/04/23')  # 也可以用setattr添加
print(people.__dict__)

people.sex = '女'  # 修改实例属性数据
print(people.__dict__)

del people.addr     # 删除一个实例属性
print(people.__dict__)

"""
    优势：当父类名改动的时候，不需要全部改动，需要修改的项减少，不用写父类名和传self。。。。
"""

class Chinese:
    """中国人的类"""

    def __init__(self, height, weight, area):
        self.height = height
        self.weight = weight
        self.area = area

    def Features(self):
        return '、、他的体重是%skg，身高是%sm' % (self.weight, self.height)

    def run(self):
        print('父类的方法.......')


class Countries(Chinese):

    def __init__(self, name, state, age, sex, height, weight, area):
        super().__init__(height, weight, area)
        self.name = name
        self.state = state
        self.age = age
        self.sex = sex

    def update(self):
        return '%s所在的国家是%s，这个国家的面积是%s' % (self.name, self.state, self.area)

    def run(self):
        super().run()       #当子类和父类方法重名时，就像要调用父类的方法的操作
        return '子类的方法'

quest = Countries('tom', 'chinese', '22', '男', 1.65, 62, '960万')
# print(quest.__dict__)
print(quest.update(),quest.Features())
print(quest.run())
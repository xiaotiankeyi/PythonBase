# class的组合
"""
概念:大类中包含小类
    使用场景:当类之间有显著的不同,并且较小的类是较大的类所需要的组件时,用组合
    2、将另外一个对象作为自己的属性成员(自己的一个属性来自于另外一个对象),这就是组合
"""


class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def admissions(self):
        return '%s学校的%s校区正在招生!!!!!' % (self.name, self.addr)


class Course(object):
    def __init__(self, name, price, period, school):
        self.name = name
        self.price = price
        self.period = period
        self.school = school


s1 = School('老男孩', '北京')
s2 = School('老男孩', '南京')
s3 = School('老男孩', '东京')

msg = '''
1 老男孩 北京校区
2 老男孩 南京校区
3 老男孩 东京校区
'''
while True:
    print(msg)
    menu = {
        '1': s1,
        '2': s2,
        '3': s3
    }
    choice = str(input('选择学校及校区>>: '))
    school_obj = menu[choice]
    print(school_obj)

    name = input('课程名>>: ')
    price = input('课程费用>>: ')
    period = input('课程周期>>: ')

    new_course = Course(name, price, period, school_obj)
    print(
        '课程%s属于%s学校,并且%s' %
        (new_course.name,
         new_course.school.name,
         # School.admissions(school_obj),
         new_course.school.admissions()
    ))
    break
print("-"*60)


# 优化后
class School(object):
    def __init__(self, school_name, addr):
        self.name = school_name
        self.addr = addr

    def admissions(self):
        return '%s学校的%s校区正在招生!!!!!' % (self.name, self.addr)


class Course(object):
    def __init__(self, name, price, period, school_name, addr):
        self.name = name
        self.price = price
        self.period = period
        self.school = School(school_name, addr)

obj = Course('java', 2000, 6, '老男孩', '上海')
val = obj.school.admissions()
# print(val)
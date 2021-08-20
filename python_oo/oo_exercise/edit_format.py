# 自定义__format__()格式

time_dic = {
    'ymd': '{0.years}:{0.month}:{0.day}',
    'mdy': '{0.month}-{0.day}-{0.years}'
}


class Date(object):
    def __init__(self, years, month, day):
        self.years = years
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        print('————>', format_spec)
        if not format_spec or format_spec not in time_dic:
            format_spec = 'ymd'
        fm = time_dic[format_spec]
        return fm.format(self)


a = Date(2019, 8, 20)
print(format(a, 'ymd'))


class Create(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        pass


user = Create('jack', 22)
print(user.__dict__)
print(hasattr(user, 'age'))
print(hasattr(user, 'jasdfpajsfamfa'))
print(dir(Create))
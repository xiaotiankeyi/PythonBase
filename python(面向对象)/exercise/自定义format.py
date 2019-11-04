time_dic = {
    'ymd' : '{0.years}:{0.month}:{0.day}',
    'mdy' : '{0.month}-{0.day}-{0.years}'
    }

class data():
    def __init__(self, years, month, day):
        self.years = years
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if not format_spec or format_spec not in time_dic:
            format_spec='ymd'
        fm=time_dic[format_spec]
        return fm.format(self)
def handle():
    a = data(2019, 8, 20)
    print(format(a,'ymd'))

#================================================
class create():
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        pass

user = create('jack', 22)
print(user.__dict__)
print(hasattr(user, 'age'))
print(hasattr(user, 'jasdfpajsfamfa'))
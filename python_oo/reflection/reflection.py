# 反射只getattr和delattr的应用

class BlackMedium(object):
    feature = 'Ugly'

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def __getattr__(self, item):
        return '你查询的属性%s不存在,运行自定义的getattr' % item

    def __delattr__(self, item):
        if item in self.__dict__:
            """判断要删除的key是否存在实例对象字典中"""
            del self.__dict__[item]
        else:
            print('你要删除的属性%s不存在,运行自定义的delattr' % item)

    def sell_house(self):
        print('%s 黑中介卖房子啦,傻逼才买呢,但是谁能证明自己不傻逼' % self.name)

    def rent_house(self):
        print('%s 黑中介租房子啦,傻逼才租呢' % self.name)


if __name__ == "__main__":
    b1 = BlackMedium('万成置地', '回龙观天露园')

    # 检测实例是否含有某属性
    print(hasattr(b1, 'name'))
    print(hasattr(b1, 'sell_house'))

    print(hasattr(b1, 'collection'))    # 注意不存在函数方法,正确输出是False,但由于自定义了__getattr__结果变为了True,原因不明

    # 获取属性
    n = getattr(b1, 'name')
    print(n)
    func = getattr(b1, 'rent_house')    # 查询实例函数并返回地址加上()可以运行
    print(func)
    func()

    getattr(b1, 'aaaaaaaa')  # 报错
    print(getattr(b1, 'aaaaaaaa',))

    # #设置属性
    setattr(b1, 'sb', True)
    setattr(b1, 'show_name', lambda self: self.name + 'sb')     # 为实例对象添加了一个实例函方法
    print(b1.__dict__)
    print('调用后面添加的实例方法:', b1.show_name(b1))

    # #删除属性
    delattr(b1, 'addr')
    delattr(b1, 'show_name')
    delattr(b1, 'show_name111')  # 不存在,则报错

    print(b1.__dict__)

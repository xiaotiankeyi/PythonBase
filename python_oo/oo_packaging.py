# 封装，私有属性，第二个层面的封装：类中把某些属性和方法隐藏起来(或者说定义成私有的)，只在类的内部使用、外部无法访问
'''
    意义在于隐藏，把类里面的数据属性隐藏起来，不让外部调用，
    _添加单下划线的目的只是起到申明作用，不应该被外部调用，行业约定协议作用
    __添加双下划线的属性python会帮我们修改属性名。。
'''


class Handle(object):
    __name = 'jack'  # 类属性被定义为私有

    def __init__(self, age, height, weight):
        self.age = age
        self.__height = height      # 实例属性定义为私有
        self.__weight = weight

    def __collection(self):     # 方法被定义为私有方法
        return '我被封装了，你没法调用哦，但是我开了接口给你，你调用接口吧'

    def interface(self):  # 提供给内部调用的__name的接口
        return '{}的身高体重指数MBI为{:.2f}%'.format(
            Handle.__name, (self.__weight / (self.__height * self.__height)))

    def func_interface(self):
        """共外部调用的接口"""
        return self.__collection()


obj = Handle('man', 1.65, 62)
print(Handle.__dict__)
print(obj.__dict__)

# print(obj._Handle__name)         # 外部强制调用被封装的私有属性
# print(obj._Handle__collection())     # 外部强制调用被封装的私有方法

print(obj.interface())          # 通过调用接口现实访问私有属性和方法
print(obj.func_interface())

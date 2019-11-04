'''
    意义在于隐藏，把类里面的数据属性隐藏起来，不让外部调用，
    _添加单下划线的目的只是起到申明作用，不应该被外部调用，约定协议作用
    __添加双下划线的属性python会帮我们修改属性名。。
'''
class handle():
    __name = 'jack'     #对数据属性进行封装

    def __init__(self, age, height, weight):
        self.age = age
        self.__height = height
        self.__weight = weight

    def __collection(self):
        return '我被封装了，你没法调用哦，但是我开了接口给你，你调用接口吧'

    def interface(self):        #提供给外部调用的__name的接口
        return '{}的身高体重指数MBI为{:.2f}%'.format(self.__name,(self.__weight / (self.__height * self.__height)))

    def func_interface(self):
        return self.__collection()

object = handle('man', 1.65, 62)
# print(handle.__dict__)
# print(object.__dict__)

# print(object._handle__name)     #强制调用被封装的数据属性
# print(object._handle__collection())   #强制调用被封装的方法

print(object.interface())
print(object.func_interface())


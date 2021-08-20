# 接口的继承
"""
    概念：
        1、在父类中定义的功能，子类在继承时必须实现，，例如父类中有read,write两个功能，在子类中必须实现这两个功能
        并且这两个功能在父类中不实现，，要在子类中实现，，父类只是起到声明的作用
        2、接口继承python没有自动帮我们实现，需要自己导相关模块。。。。。。
        3、接口类不需要实现内部逻辑，规范子类，不需要实例化
        4、导入模块abc，给父类2个属性加上装饰器之后，如果子类再少属性的话，就直接报错了，这样就强制性的约束了子类必须有父类的2个方法了
"""
import abc


class All_file(metaclass=abc.ABCMeta):  # 调用该方法后，子类必须实现父类所声明的功能，起限定功能
    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def write(self):
        pass


class Men(All_file):
    def read(self):
        return 'men, read'

    def write(self):
        return 'man write'


class Disk(All_file):
    def read(self):
        return "disk read"

    def write(self):
        return 'disk write'

if __name__ == "__main__":
    mode = Disk()
    print(mode.write())
    print(mode.read())

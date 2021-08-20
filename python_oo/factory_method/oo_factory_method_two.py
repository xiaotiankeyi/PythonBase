# 工厂方法模式优缺点

# 优点：更符合开闭原则，增加一个产品类，则只需要实现其他具体的产品类和具体的工厂类即可；符合单一职责原则，每个工厂只负责生产对应的产品
# 缺点：增加一个产品，就需要实现对应的具体工厂类和具体产品类；每个产品需要有对应的具体工厂和具体产品类

from abc import ABC, abstractmethod


# 抽象工厂
class AbastractFactory(ABC):
    """作为工厂基类，定义好产品工厂必须要的功能，子类实现功能"""
    @abstractmethod
    def product_phone(self):
        pass

    @abstractmethod
    def game(self):
        pass

# 苹果工厂
# class AppleFactory(AbastractFactory):
#
#     def product_phone(self):
#         return Apple().make()


# 小米工厂
class XiaomiFactory(AbastractFactory):
    """子工厂继承声明的功能"""
    def product_phone(self):
        return XiaoMi().make()

    def game(self):
        return XiaoMi().game()


# 生产线
class Phone(ABC):
    """作为基类生产线，定义好子类生产线必须要有的功能"""
    @abstractmethod
    def make(self):
        pass

    @abstractmethod
    def game(self):
        pass

# 苹果生产线
# class Apple(Phone):
#
#     def make(self):
#         print("make apple")


# 小米生产线
class XiaoMi(Phone):
    """继承基类生产线，子类实现功能"""
    def make(self):
        print("make xiaomi")

    def game(self):
        print("小米手机支持玩游戏！！！")

def client_product(factory: AbastractFactory):
    # print("返回工厂函数地址:", factory)
    return factory


if __name__ == '__main__':
    xiaomi = client_product(XiaomiFactory())
    xiaomi.product_phone()
    xiaomi.game()
    # apple = client_product(AppleFactory())
    # apple.product_phone()

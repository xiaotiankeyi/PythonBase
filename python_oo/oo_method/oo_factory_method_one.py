# 工厂模式Factory Method
# 简单工厂模式优缺点
# 优点:客户端与产品的创建分离,客户端不需要知道产品创建的逻辑,只需要消费该产品即可,
# 缺点:工厂类集成了所有产品的创建逻辑,当工厂类出现问题,所有产品都会出现问题;还有当新增加产品都会修改工厂类,违背开闭原则
from abc import ABC, abstractmethod


# 手机
class Phone(ABC):
    """基类,声明生产的手机必须要的功能,在接下来的子类中实现具体功能"""
    @abstractmethod
    def make(self):
        pass


# 苹果手机
class Apple(Phone):

    def make(self):
        print("make apple")


# 小米手机
class XiaoMi(Phone):

    def make(self):
        print("make xiaomi")


class Factory:
    """生产工厂类,集成产品的创建逻辑"""
    def product_phone(self, mobile_type):
        if mobile_type == 'apple':
            return Apple()
        else:
            return XiaoMi()


if __name__ == '__main__':
    factory = Factory()
    a = factory.product_phone('apple')
    a.make()
    factory.product_phone('xiaomi').make()

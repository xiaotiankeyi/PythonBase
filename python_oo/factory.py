#工厂模式


class ComputerFactory:
    """工厂对象"""
    def accept(self, computer):
        if computer == '联想':
            return Lenovo()
        else:
            pass


class Computer(object):
    """电脑父类"""
    def calculatte(self):
        pass

class Lenovo(Computer):
    count = 0

    def output(self):
        print("生产一条联想电脑.....")

    def calculatte(self):
        print('输出', self.count)

if __name__ == "__main__":
    a = ComputerFactory()
    lx = a.accept("联想").output()
# 实现类装饰器,为函数增加新的功能

class Family(object):
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        self.new()
        result = self.__func()
        print(result)

    def new(self):
        print('所要执行的新的功能!!!')


@Family
def daughter():

    return '需要被装饰得类.....'


if __name__ == "__main__":

    daughter()

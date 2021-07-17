# 类的形式实现线程

from threading import Thread
from time import sleep
import os


class Function(Thread):

    def __init__(self, value):
        # Thread.__init__(self)
        super(Function, self).__init__()
        self.value = value

    def run(self):
        sleep(1)
        print('hello, hao are yuo {}\t'.format(self.value), os.getpid())


if __name__ == "__main__":

    # 创建线程
    t1 = Function('t1')
    t2 = Function('t2')

    # 启动线程
    t1.start()
    t2.start()

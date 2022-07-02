# 自定义实现class实现线程方法

from threading import Thread
from time import sleep
import os


class Function(Thread):

    def __init__(self, value):
        # 继承父类
        # Thread.__init__(self)
        super(Function, self).__init__()
        self.value = value

    def run(self):
        sleep(1)
        print('hello, hao are yuo {}\t'.format(self.value), os.getpid())


if __name__ == "__main__":
    threads = []
    # 创建线程
    t1 = Function('t1')
    t2 = Function('t2')

    # 启动线程
    t1.start()
    t2.start()
    threads.append(t1)
    threads.append(t2)

    for t in threads:
        t.join()

    print("当前py文件进程:", os.getpid(), os.getppid())

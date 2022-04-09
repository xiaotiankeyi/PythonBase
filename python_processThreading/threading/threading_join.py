# join
# 主线程不等子线程,会先提前结束运行,可以通过join等待子进程
import threading
from threading import Thread
from time import sleep, time
import os


class threadFunction(Thread):
    def __init__(self, name):
        super(threadFunction, self).__init__()
        self.name = name

    def run(self):
        sleep(2)
        print('hello hao are you {}\t'.format(self.name), os.getpid())


if __name__ == "__main__":

    print(threading.currentThread())

    t = threadFunction('lucy')
    t1 = threadFunction('value')

    # 开始计时
    date_start = time()
    t.start()
    t1.start()

    t.join()  # 子线程输出后在输出主线程
    t1.join()

    # 结束计时
    date_end = time() - date_start
    print('所用时间:{}'.format(date_end))

    print('主线程:{}'.format(os.getpid()))

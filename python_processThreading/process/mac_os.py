import multiprocessing
import os
from multiprocessing import Process

print('当前.py文件的id:', os.getpid())


def a():
    print('父进程id继承pycharm编辑器:%s' % os.getppid(), '函数a本身的id继承当前py文件的id:', os.getpid())


def b():
    print('b函数父进程id继承当前py文件的id:%s' % os.getppid(), '函数b本身的id:', os.getpid())


if __name__ == "__main__":
    """设置启动进程的方法为fork后,子进程只执行b函数内的代码"""
    # multiprocessing.set_start_method("fork")
    multiprocessing.set_start_method("spawn")


    a()

    p = Process(target=b, args=())
    p.start()
    p.join()
    print('结束')

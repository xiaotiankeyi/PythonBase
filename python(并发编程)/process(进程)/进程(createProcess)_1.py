"""通过队列来进行进程通讯"""
import os
import random
# print(os.cpu_count())   #查看本机cpu

from multiprocessing import Process  # multiprocessing"矛体帕赛醒"


def func(name=None):
    print("主进程.......", os.getppid())
    print("子进程.......", os.getpid())


if __name__ == "__main__":
    func("tom")
    print("=" * 20)

    p1 = Process(target=func, args=("jack",))
    p1.start()
    print(p1.name, p1.pid)

    p1.join()

    print("解释器进程", os.getppid())

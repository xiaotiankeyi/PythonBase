# 进程通信
import multiprocessing
import os
import time
from multiprocessing import Pipe


def foo(q1):
    time.sleep(1)
    print("子进程", os.getpid())
    print('获得主进程添加的值--{}'.format(q1.recv()))
    q1.send('子进程添加的数字{}'.format(123))


if __name__ == '__main__':
    # 主进程运行部分
    print("主进程", os.getpid())
    q1, q2 = Pipe()  # p1传递给子线程，p2主进程运行
    q2.send('主进程添加了{}'.format(os.getpid()))

    # 子进程运行部分
    p = multiprocessing.Process(target=foo, args=(q1,))  # 把主进创建的q1传递给子进程
    p.start()
    p.join()

    print('主进程{}获取{}'.format(os.getpid(), q2.recv()))

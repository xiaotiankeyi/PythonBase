# manager数据共享管理,下面例示通过创建多进程的方式来做减法运算

import os
from multiprocessing import Manager, Lock
from multiprocessing import Process


def f(d, l, lock):
    with lock:
        print(f"子进程{os.getpid()}开始做减法时count等于{d}")
        d["count"] -= 1
        print(os.getppid(), "{0}子线程做减法后count等于{1}".format(os.getpid(), d))
        l.append(d['count'])


if __name__ == '__main__':
    print("编辑器主进程{}".format(os.getppid()))
    print('py文件进程{}'.format(os.getpid()))

    lock = Lock()
    with Manager() as manager:

        d = manager.dict({"count": 100})
        l = manager.list()
        p_list = []

        for i in range(10):
            p = Process(target=f, args=(d, l, lock))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print('函数进程{}获取{}'.format(os.getpid(), l))

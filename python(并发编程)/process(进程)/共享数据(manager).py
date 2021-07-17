# manager数据共享管理,下面例示通过创建多进程的方式来做减法运算

import os
from multiprocessing import Manager, Lock
from multiprocessing import Process


def f(d, l, lock):
    with lock:
        d["count"] -= 1
        print(os.getppid(), "{1}子线程{0}".format(d, os.getpid()))
        l.append(d['count'])

if __name__ == '__main__':
    print("编辑器主进程{}".format(os.getppid()))
    print('函数进程{}'.format(os.getpid()))

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

        print('函数进程{}获取{}'.format(os.getpid(),l))
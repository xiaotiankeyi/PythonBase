# 在进程之间交换对象通信方式一 列队
# 优点：可以进行并发执行，空间独立，数据安全
# 缺点：创建和删除时占用资源多
# 以下例子实现父进程和子进程之间的数据通信
import os
import queue
import time
import multiprocessing


def foo(q):
    time.sleep(1)
    print("子进程", os.getpid())
    print('获得主进程添加的值--{}'.format(q.get()))

    q.put('子进程添加的数字{}'.format(123))


if __name__ == '__main__':
    # 主进程运行部分
    print("主进程", os.getpid())
    # q = queue.Queue()   # 线程中的Queue不能在进程中用
    q = multiprocessing.Queue()
    q.put('主进程添加了{}'.format(os.getpid()))

    # 子进程运行部分
    p = multiprocessing.Process(target=foo, args=(q,))  # 把主进创建的q传递给子进程
    p.start()
    p.join()

    print('主进程{}获取{}'.format(os.getpid(), q.get()))

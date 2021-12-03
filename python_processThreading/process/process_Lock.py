# 进程Lock同步锁
# 作用,以使用锁来确保一次只有一个进程打印到标准输出,不使用锁的情况下，来自于多进程的输出很容易产生混淆。
import multiprocessing
from multiprocessing import Process, Lock
import time


def f(l, i):
    try:
        l.acquire()
        time.sleep(0.5)
        print('hello world %s' % i)
    except Exception as err:
        print(err)
    finally:
        l.release()


if __name__ == "__main__":
    """解决FileNotFoundError: [Errno 2] No such file or directory发方法一,更换启动方式"""
    # multiprocessing.set_start_method("fork")
    # lock = Lock()

    # for num in range(5):
    #     Process(target=f, args=(lock, num)).start()


    """解决方法二,缺点是顺序会乱"""
    lock = Lock()
    processList = []
    for i in range(5):
        p = Process(target=f, args=(lock, i))
        processList.append(p)
        p.start()

    for j in processList:
        j.join()
# 同步锁，先指定一个线程运行完,在运行下一个进程。实现一个一个的运行，保证数据安全"""
# 同步锁，互斥锁，指定线程串新运行，单线程运行"""


import threading
import time


def sub():
    global num

    # 获得一个锁
    print("当前执行的是:", threading.current_thread().getName())
    lock.acquire()

    temp = num
    time.sleep(0.01)  # 只有这三部分是单线程执行,对公共数据的操作，这是需要保护数据安全的部分
    num = temp - 1

    # 释放锁
    lock.release()


num = 100
if __name__ == "__main__":
    l = []
    lock = threading.Lock()  # 创建锁

    start_date = time.time()
    for i in range(100):
        t = threading.Thread(target=sub, args="", )
        l.append(t)
        t.start()

    for t in l:
        t.join()  # 阻拦主线程运行

    end_date = time.time()
    print(
        '主线程是运行:{},num是:{}'.format(
            (end_date - start_date),
            num))  # 获取子线程的数据,和子线程数据同步

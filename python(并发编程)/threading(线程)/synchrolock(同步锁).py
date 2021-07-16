"""同步锁，互斥锁，指定线程串新运行，单线程运行"""
import threading
import time
import time


def sub():
    global num
    print("当前执行的是:", threading.current_thread().getName())
    lock.acquire()
    temp = num
    time.sleep(0.01)  # 只有这三部分是单线程执行,对公共数据的操作
    num = temp - 1
    lock.release()


num = 100
if __name__ == "__main__":
    l = []
    lock = threading.Lock()  # 创建锁

    start_date = time.time()
    for i in range(100):
        t = threading.Thread(target=sub)
        l.append(t)
        t.start()

    for t in l:
        t.join()  # 阻拦主线程运行

    end_date = time.time()
    print(
        '主线程是运行:{},num是:{}'.format(
            (start_date - end_date),
            num))  # 获取子线程的数据,和子线程数据同步

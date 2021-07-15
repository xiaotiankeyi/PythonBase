# for循环批量开启进程
import threading
from time import sleep, time
import os


def handle(parameter):
    sleep(1)
    print('hello, hao are yuo {}'.format(parameter), os.getpid())


if __name__ == "__main__":
    print('当前进程是{}'.format(threading.currentThread()))

    date_start = time()

    # 创建线程
    thread_list = []
    for i in range(8):
        t = threading.Thread(target=handle, args=(f'value{i + 1}',))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    date_end = time() - date_start
    print('时间是：{}'.format(date_end))
    print('主线程是:{}'.format(os.getpid()))

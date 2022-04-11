# 主线程和子线程之间的数据共享,以下例子通过子线程来改变主线程的值
import threading
from threading import Thread
import os


def work():
    global n
    n = 10
    print(f'子线程->{t.ident}的n是:', n)
    print('当前运行的线程数:', threading.activeCount())
    print('当前运行的线程数:', threading.active_count())


def inputValue(n):
    print(f"通过子线程—>{t.ident}获取主线程的值,需要把值传给子线程{n}")


if __name__ == "__main__":
    n = 100
    print('主线程:{}的n是{}'.format(os.getpid(), n), )  # 主线程查看结果为10,取的值是本身为改变的值

    t = Thread(target=inputValue, args=(n,))
    t.start()
    t.join()

    t1 = Thread(target=work, args="",)
    t1.start()
    t1.join()

    print('主线程:{}的n是{}'.format(os.getpid(), n), )  # 主线程查看结果为10, 取得值是子线程改变后里的值

# 数据共享
from threading import Thread
import os


def work():
    global n
    n = 10
    print(f'子线程{t.ident}的n是:', n)


if __name__ == "__main__":
    n = 100
    t = Thread(target=work,)
    t.start()
    t.join()

    print('主线程：{}的n是{}'.format(os.getpid(), n),)  # 主线程查看结果为10, 取得值是子线程里的n

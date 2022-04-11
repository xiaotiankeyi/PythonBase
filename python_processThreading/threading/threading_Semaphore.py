# 信号量
"""
概念:
    不需要保证数据安全的情况下信息量用来控制线程并发数,可以指定若干个线程来处理数据,信号量也是同步的,也是锁得一种
"""
import threading
import time


class myThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(3)
            semaphore.release()


if __name__ == "__main__":
    semaphore = threading.Semaphore(2)  # 最大连接数为2

    th = []
    for i in range(10):
        th.append(myThread())

    for t in th:
        t.start()

# 生产者消费者模式，保持相互之间的平衡

from threading import Thread
from queue import Queue
from time import sleep

def service():
    num = 1
    while Queue(maxsize=10):
        print('生产了{}杯奶茶'.format(num))
        data.put(f'第{num}杯奶茶')
        num += 1
        sleep(1)

def client():
    print('购买了{}.....'.format(data.get()))
    sleep(2)

if __name__ == "__main__":
    data = Queue(maxsize=10)

    t1 = Thread(target=service, args="",)
    t2 = Thread(target=client, args="",)
    t3 = Thread(target=client, args="",)

    t1.start()
    t2.start()
    t3.start()
"""
3个生产者线程循环生成12个包子,创建12个消费者线程进行消费。实现等价消费
"""
import time
import queue
import threading
import os

q = queue.Queue(10)     # 生成一个队列,用来保存“包子”,最大数量为10

def productor(i):
    # 厨师不停地每2秒做一个包子
    while True:
        q.put("厨师 %s 做的包子！%s" % (i, threading.current_thread().getName()))
        time.sleep(2)

def consumer(j):
    # 顾客不停地每秒吃一个包子
    # while True:
        print("顾客 %s, %s 吃了一个 %s"%(j, threading.current_thread().getName(), q.get()))
        time.sleep(1)

if __name__ == "__main__":

    # 实例化了3个生产者(厨师)
    for i in range(3):
        t = threading.Thread(target=productor, args=(i,))
        t.setDaemon(True)   # 这设置守护进程
        t.start()

    threads_client = []
    # 实例化了10个消费者(顾客)
    for j in range(12):
        v = threading.Thread(target=consumer, args=(j,))
        v.start()
        threads_client.append(v)
    
    for th in threads_client:
        th.join()

    if q.empty():
        print(q.full())
        print(q.qsize())
        print(threading.active_count())

        print(f"主进程{os.getpid()}结束了....")


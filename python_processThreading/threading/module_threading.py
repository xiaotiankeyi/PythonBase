"""
进程概念:
    进程就是一个程序在一个数据集上的一次动态执行过程
    组成:程序,数据集,进程控制块三部分
    进程是最小的资源单位,通信难,切换消耗大
    线程是最小的执行单位
    线程与线程之间可以共用进程数据,共享的
"""
import threading
import time
import os
from threading import local

def Hi(num):
    print("hello %d" % num)
    time.sleep(1)

# 特殊的对象
lqz = local()
def task(arg):
    # 对象.val = 1/2/3/4/5
    lqz.value = arg
    time.sleep(2)
    print('——>', lqz.value)
for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()

if __name__ == '__main__':
    threads = []

    t1 = threading.Thread(target=Hi, args=(10,))  # 创建了一个线程对象t1
    t2 = threading.Thread(target=Hi, args=(9,))  # 创建了一个线程对象t1

    t1.start()
    t2.start()
    threads.append(t1)
    threads.append(t2)

    for t in threads:
        t.join()   # 等待所有线程完成,再运行主线程,

    print("\nending..........", os.getpid(), os.getppid(), end='\t')


    def record():
        """threading way threading 对象方法"""
        t1.run()  # 用于表示线程活动方法
        t1.start()  # 启动线程活动
        t1.getName()  # 返回线程名
        t1.setName(" ")  # 设置线程名
        t1.setDaemon(True)  # 守护线程
        t1.join()  # 等待线程执行完,才运行主线程
        """threading module way"""
        threading.activeCount()  # 返回正在运行的线程数
        threading.active_count()  # 统计正在运行的线程数


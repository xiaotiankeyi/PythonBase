"""
进程概念：
    进程就是一个程序在一个数据集上的一次动态执行过程
    组成：程序，数据集，进程控制块三部分
    进程是最小的资源单位，通信难,切换消耗大
    线程是最小的执行单位
    线程与线程之间可以共用进程数据，共享的
"""
import threading  # 线程
import time


def Hi(num):
    print("hello %d" % num)
    time.sleep(3)


if __name__ == '__main__':

    t1 = threading.Thread(target=Hi, args=(10,))  # 创建了一个线程对象t1
    t1.start()

    # t1.join()   #t1没完成就不运行主线程，

    t2 = threading.Thread(target=Hi, args=(9,))  # 创建了一个线程对象t1
    t2.start()

    print("\nending..........")

    def record():
        """threading way threading 对象方法"""
        t1.run()  # 用于表示线程活动方法
        t1.start()  # 启动线程活动
        t1.isAlive()  # 返回线程是否是活动的
        t1.getName()  # 返回线程名
        t1.setName(" ")  # 设置线程名
        t1.setDaemon(True)  # 守护线程
        t1.join()  # 等待线程执行完，才运行主线程
        """threading module way"""
        threading.activeCount()  # 返回正在运行的线程数
        threading.active_count()  # 统计正在运行的线程数
pass

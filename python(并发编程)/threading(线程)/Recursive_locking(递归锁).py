import threading
import time

'''递归锁是解决死锁的问题.......'''


class MyThread(threading.Thread):

    def actionA(self):
        R_Lock.acquire()
        print(self.name, "gotA", time.ctime())
        time.sleep(2)

        R_Lock.acquire()
        print(self.name, "gotB", time.ctime())
        time.sleep(1)

        R_Lock.release()
        R_Lock.release()

    def actionB(self):
        R_Lock.acquire()
        print(self.name, "gotB", time.ctime())
        time.sleep(2)

        R_Lock.acquire()
        print(self.name, "gotA", time.ctime())
        time.sleep(1)

        R_Lock.release()
        R_Lock.release()

    def run(self):
        self.actionA()
        self.actionB()


if __name__ == '__main__':

    R_Lock = threading.RLock()  # 创建递归锁#一个线程拿到锁,counter加1,该线程内又碰到加锁的情况，
<<<<<<< HEAD:python(线程)/threading(线程)/Recursive_locking(递归锁).py
    # 则counter继续加1,这期间所有其他线程都只能等待，等待该线程释放所有锁，即counter递减到0为止
=======
                                # 则counter继续加1,这期间所有其他线程都只能等待，等待该线程释放所有锁，即counter递减到0为止
>>>>>>> 187e17d4165ca38917f3d395f9401a4f86e328a6:python(并发编程)/threading(线程)/Recursive_locking(递归锁).py
    L = []

    for i in range(5):
        t = MyThread()
        L.append(t)
        t.start()

    for i in L:
        i.join()

    print("ending....")

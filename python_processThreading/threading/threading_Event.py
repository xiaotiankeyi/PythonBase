# Event创建事件管理标志,事件满足为True,不满足为false
# threading.Event可以使一个线程等待其他线程的通知,其内置了一个标志,初始值为False
"""
方式解读:event.set()事件设置为True,event.clear()事件为False,
        event.is_set()判断事件标志是否为True,event.wait(timeout=None)调用该方式的线程会被阻塞,超时后,线程会停止阻塞继续执行
"""
import threading
import time


class Boss(threading.Thread):

    def run(self):
        print("BOSS:今晚大家都要加班到22:00,")
        print(event.isSet())  # False   返回event的状态值
        event.set()  # 设置为True

        time.sleep(3)
        print("BOSS:<22:00>可以下班了,")
        print(event.isSet())  # 返回event的状态值
        event.set()


class Worker(threading.Thread):
    def run(self):
        event.wait()  # 一旦event.wait被设定,等同于pass,进入等待状态
        print("Worker:哎……命苦啊！")
        event.clear()  # 设置为False

        event.wait()
        print("Worker:OhYeah!")


if __name__ == "__main__":
    event = threading.Event()

    threads = []
    for i in range(5):
        threads.append(Worker())
    threads.append(Boss())

    print(threads)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("ending.....")

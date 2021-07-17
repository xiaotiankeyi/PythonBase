"""关于setDaemon(守护线程)
需求：主线程完成了，子线程不管你完成没完成也结束，所以子线程要设置为守护线程
"""
import threading
from time import ctime, sleep


def ListenMusic(name):
    print("Begin listening to %s. %s" % (name, ctime()))
    sleep(3)
    print("end listening %s" % ctime(), "结束")


def RecordBlog(title):
    print("Begin recording the %s! %s" % (title, ctime()))
    sleep(5)
    print('end recording %s' % ctime(), '结束')


if __name__ == '__main__':
    threads = []

    t1 = threading.Thread(target=ListenMusic, args=('水手',))
    t2 = threading.Thread(target=RecordBlog, args=('python线程',))

    threads.append(t1)
    threads.append(t2)

    t2.setDaemon(True)  # 子线程守护(跟随)主线程, 当主线程关闭, 子线程t1,t2就马上关闭
    t1.setDaemon(True)

    for t in threads:
        t.start()

    print("\n主线程关闭：all over %s" % ctime())  # 属于主线程的内容
    pass

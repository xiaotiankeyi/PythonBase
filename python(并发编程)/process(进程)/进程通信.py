# import queue,time
#
# import multiprocessing
# def foo(q):
#     time.sleep(1)
#     print("son process",id(q))
#     q.put(123)
#     q.put("yuan")
#
# if __name__ == '__main__':
#     #q=queue.Queue()
#     q=multiprocessing.Queue()
#     p=multiprocessing.Process(target=foo,args=(q,))
#     p.start()
#     #p.join()
#     print("main process",id(q))
#     print(q.get())
#     print(q.get())

from multiprocessing import Process, Manager,Lock
import os


def f(d, lock):
    with lock:
        d["count"] -= 1
        print(os.getppid(),"子线程", d, os.getpid())


if __name__ == '__main__':
    lock = Lock()
    with Manager() as manager:

        d = manager.dict({"count": 100})

        p_list = []

        for i in range(10):
            p = Process(target=f, args=(d, lock))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d,os.getppid())

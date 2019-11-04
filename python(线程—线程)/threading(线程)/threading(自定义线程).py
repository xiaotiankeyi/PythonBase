'''自定义线程开启方式'''
from threading import Thread
from time import sleep
import os

class threadFunction(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(1)
        print('hello hao are you {}'.format(self.name), os.getpid())

if __name__ == "__main__":
    t = threadFunction('lucy')
    t.start()
    t.join()    #子线程输出后在输出主线程

    print('主线程:{}'.format(os.getpid()))
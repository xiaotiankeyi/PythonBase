import threading
from time import sleep, ctime
import os

def handle(parameter):
    sleep(1)
    print('hello, hao are yuo {}'.format(parameter),os.getpid())

def crray(parameter):
    sleep(1)
    print('hello, hao are yuo {}'.format(parameter),os.getpid())


if __name__ =="__main__":
    t = threading.Thread(target=handle, args=('jack',))
    t2 = threading.Thread(target=crray, args=('lucy',))
    t.start()
    t2.start()

    print('主线程是:{}'.format(os.getpid()))

    '''
    在进程下开启的每个线程都和主进程的pid一样.....
    '''
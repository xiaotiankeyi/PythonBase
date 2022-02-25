import threading
from unittest import result
import requests
import os
import time

"""比较多线程和单线程的区别"""

urls = [
    f'https://www.cnblogs.com/#p{num}'
        for num in range(1, 51)
]


def craw(url):
    data = requests.get(url=url)
    data = data.text
    t_name = threading.currentThread()
    print((os.getpid(), t_name, url, len(data)))

def singleThreading():
    """单线程启动"""
    for url in urls:
        craw(url)

def manyThreading():
    """多线程运行"""
    threadings = []

    for url in urls:
        threadingObj = threading.Thread(target=craw, args=(url,))
        threadings.append(threadingObj)
    
    for tobj in threadings:
        tobj.start()

    for tobj in threadings:
        tobj.join()

if __name__ == "__main__":
    pass
    # print(urls)

    # print('start time')
    # start = time.time()
    # singleThreading()
    # stop = time.time()
    # print('time consuming', stop - start, 's')


    print('start time')
    start = time.time()
    manyThreading()
    stop = time.time()
    print('time consuming', stop - start, 's')
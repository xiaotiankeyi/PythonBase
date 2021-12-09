# 实战,实现用户输入字母后就用子线程进行大写转化,在开一个子线程对其保存
import threading
from threading import Thread
import sys
import os
import time

msg_l = []
format_l = []


def talk():  # 该线程输入

    while True:
        pid = os.getpid()
        threadingInfo = threading.enumerate()
        print('------- Running threads On Pid: %d -------' % pid)
        for t in threadingInfo:
            print(t.name, t.ident)
        print()
        time.sleep(1)
        msg = input('>>: ').strip()
        if not msg:
            continue
        elif msg == 'exit':
            sys.exit()
        msg_l.append(msg)


def format_msg(msgData):  # 该线程转化大写
    while True:
        if msgData:
            res = msgData.pop()
            format_l.append(res.upper())


def save(formatData):  # 该线程保存到文件
    while True:
        if format_l:
            with open('data.dat', 'a', encoding='utf-8') as f:
                res = formatData.pop()
                f.write('%s\n' % res)


if __name__ == '__main__':

    t2 = Thread(target=format_msg, args=(msg_l,))
    t3 = Thread(target=save, args=(format_l,))

    threads = []
    threads.append(t2)
    threads.append(t3)

    for d in threads:
        d.setDaemon(True)

    for s in threads:
        s.start()

    talk()

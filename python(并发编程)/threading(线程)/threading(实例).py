from threading import Thread
msg_l = []
format_l = []


def talk():  # 该线程输入
    while True:
        msg = input('>>: ').strip()
        if not msg:
            continue
        msg_l.append(msg)


def format_msg():  # 该线程转化大写
    while True:
        if msg_l:
            res = msg_l.pop()
            format_l.append(res.upper())


def save():  # 该线程保存到文件
    while True:
        if format_l:
            with open('data.dat', 'a', encoding='utf-8') as f:
                res = format_l.pop()
                f.write('%s\n' % res)


if __name__ == '__main__':
    t1 = Thread(target=talk)
    t2 = Thread(target=format_msg)
    t3 = Thread(target=save)
    t1.start()
    t2.start()
    t3.start()

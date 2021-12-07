# 实现协程功能
from greenlet import greenlet

print(dir(greenlet))
"""
Greenlet是python的一个C扩展，来源于Stackless python，旨在提供可自行调度的‘微线程’， 即协程。
generator实现的协程在yield value时只能将value返回给调用者(caller)。 
而在greenlet中，target.switch（value）可以切换到指定的协程（target）， 
然后yield value。greenlet用switch来表示协程的切换，从一个协程切换到另一个协程需要显式指定。
"""


def sister(val):
    print(f"1.我是{val},你是谁。。")
    g2.switch('堂弟')
    print('3.你在干吗？？')
    g2.switch()


def cousin(val):
    print(f"2.我是{val}")
    g1.switch()
    print('4.我在玩游戏！！')
    # raise NameError


# 生产者消费者模型
def consumer():
    last = ''
    while True:
        receival = pro.switch(last)
        if receival is not None:
            print('Consume %s' % receival)
            last = receival


def producer(n):
    con.switch()
    x = 0
    while x < n:
        x += 1
        print('Produce %s' % x)
        last = con.switch(x)


if __name__ == "__main__":
    g1 = greenlet(sister)
    g2 = greenlet(cousin)

    # 切换函数执行
    g1.switch('姐姐')

    pro = greenlet(producer)
    con = greenlet(consumer)
    pro.switch(5)

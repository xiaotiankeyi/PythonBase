from gevent import monkey  # 为了能识别time等模块的io
monkey.patch_all()

from time import time, sleep
import gevent


"""
当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。
由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。
"""

def sister(val):
    print(f"1.我是{val},你是谁。。")
    # gevent.sleep(2)
    sleep(1)
    print('3.你在干吗？？')


def cousin(val):
    print(f"2.我是{val}")
    # gevent.sleep(2)
    sleep(0.5)
    print('4.我在玩游戏！！')


if __name__ == "__main__":

    start_date = time()
    # 创建对象
    g1 = gevent.spawn(sister, '姐姐')
    g2 = gevent.spawn(cousin, '堂弟')

    # 切换函数执行,开启任务
    # g1.join()
    # g2.join()
    gevent.joinall([g1, g2])


    end_date = time()
    print(end_date - start_date)

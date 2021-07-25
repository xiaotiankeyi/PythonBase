from gevent import monkey  # 为了能识别time等模块的io
monkey.patch_all()

from time import time, sleep
import gevent


def sister(val):
    print(f"1.我是{val},你是谁。。")
    # gevent.sleep(2)
    sleep(2)
    print('3.你在干吗？？')


def cousin(val):
    print(f"2.我是{val}")
    # gevent.sleep(2)
    sleep(2)
    print('4.我在玩游戏！！')


if __name__ == "__main__":

    start_date = time()
    # 创建对象
    g1 = gevent.spawn(sister, '姐姐')
    g2 = gevent.spawn(cousin, '堂弟')

    # 切换函数执行,开启任务
    g1.join()
    g2.join()

    end_date = time()
    print(end_date - start_date)

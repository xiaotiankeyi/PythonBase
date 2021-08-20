# 实现协程功能
from greenlet import greenlet


def sister(val):
    print(f"1.我是{val},你是谁。。")
    g2.switch('堂弟')
    print('3.你在干吗？？')
    g2.switch()


def cousin(val):
    print(f"2.我是{val}")
    g1.switch()
    print('4.我在玩游戏！！')


if __name__ == "__main__":
    g1 = greenlet(sister)
    g2 = greenlet(cousin)

    # 切换函数执行
    g1.switch('姐姐')

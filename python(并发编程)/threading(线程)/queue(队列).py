# 概念： 针对多线性应用，队列是一种数据结构，

import queue  # 线程队列


def one():
    q = queue.Queue(4)  # 三种储存取值模式，先进先出

    # 方法
    # print(q.qsize())  # 队列大小
    # print(q.empty())  # 是否为空
    # print(q.full())  # 是否满

    # 存放数据
    q.put(12)
    q.put("hello")
    q.put({"name": "yuan"})

    for i in range(4):
        # q.get(block=False)   读取数据，队列为空时不报错
        data = q.get(block=True, timeout=2)
        # data = q.get_nowait()   #队列为空时报错
        print(data)
        print("----------")


def two():
    a = queue.LifoQueue()  # 先进后出模式
    a.put(12)
    a.put("hello")
    a.put({"name": "yuan"})

    for i in range(4):
        data = a.get(block=True, timeout=2)
        print(data)
        print("----------")


def three():
    # 优先级，根据设定好的索引取值
    f = queue.PriorityQueue()
    f.put((1, 12))
    f.put((3, "hello"))
    f.put((2, {"name": "yuan"}))

    for i in range(4):
        data = f.get(block=True, timeout=2)
        print(data)
        print("----------")


if __name__ == "__main__":
    # one()
    # two()
    three()

"""
概念：
    针对多线性应用，队列是一种数据结构，
"""
import queue  # 线程队列

q = queue.Queue(4)  # 三种储存取值模式，先进先出，先进后出，优先级
q.put(12)
q.put("hello")
q.put({"name": "yuan"})

#方法
print(q.qsize())    #队列大小
print(q.empty())    #是否为空
print(q.full())     #是否满

while 1:
    data = q.get()   #q.get(block=False)   取不到值就报错
    print(data)
    print("----------")

import queue

a = queue.LifoQueue     #先进后出模式
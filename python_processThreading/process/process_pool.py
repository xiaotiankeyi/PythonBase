# 进程池 pool
# 避免了频繁的开启和销毁进程,提高效率,节省空间和时间
# 如果要启动大量的子进程,可以用进程池的方式批量创建子进程:

import time
from multiprocessing import Pool
import os
import random


def Foo(task):
    start = time.time()
    time.sleep(random.randint(1, 5))
    end = time.time()

    # print(f"父进程:{os.getppid()}, 子进程:{os.getpid()},任务【{task}】完成时间为{end - start}s")     # 同步调用
    return f"父进程:{os.getppid()}, 子进程:{os.getpid()},任务【{task}】完成时间为{end - start}s"  # 异步调用并使用回调


def Bas(bas):
    """接收Foo返回的字符"""
    print(os.getppid(), "result", os.getpid(), "|", bas)

if __name__ == "__main__":
    systemStart = time.time()
    p = Pool(5)

    task = ["游戏", "吃饭", "睡觉", "拖地", "洗衣服", "学习", "上厕所", "看视频"]
    for i in task:
        res = p.apply_async(func=Foo, args=(i,), callback=Bas)  # 异步调用并使用回调
        # res = p.apply(func=Foo, args=(i,))  # 同步调用

    p.close()  # 关闭进程池
    p.join()  # 回收进程池

    print('本机核数', os.cpu_count())
    systemEnd = time.time()
    print(f"总的运行时长{systemEnd - systemStart}s")

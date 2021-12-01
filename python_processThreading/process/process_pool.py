# 避免了频繁的开启和销毁进程，提高效率，节省空间和时间
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

import time
from multiprocessing import Pool
import os


def Foo(i):
    # time.sleep(1)
    print(os.getppid(), "result", i, os.getpid())
    return "Hello print result is %s" % i


def Bas(bas):
    """接收Foo返回的字符"""
    print(os.getppid(), "result", os.getpid(), bas)


if __name__ == "__main__":
    p = Pool(5)

    result = []
    for i in range(12):
        # res = p.apply_async(func=Foo, args=(i,), callback=Bas)  # 异步调用并使用回调
        # res = p.apply(func=Foo, args=(i,))  # 同步调用
        res = p.apply_async(func=Foo, args=(i,))  # 异步调用
        result.append(res)

    p.close()  # 关闭进程池
    p.join()  # 回收进程池

    print("end,,,,,,,", os.getpid())
    print('本机核数', os.cpu_count())

# 避免了频繁的开启和销毁进程，提高效率，节省空间和时间

import time
from multiprocessing import Pool

def Foo(i):
    time.sleep(1)
    print("result", i)
    return "Hello print result is %s" % i

def Bas(bas):
    """接收Foo返回的字符"""
    print(bas)


if __name__ == "__main__":
    p = Pool(5)

    result = []
    for i in range(10):
        res = p.apply_async(func=Foo, args=(i,), callback=Bas)  # 异步调用
        res = p.apply(func=Foo, args=(i,))      #同步调用
        result.append(res)

    p.close()       # 关闭进程池
    p.join()    # 回收进程池

    print("end,,,,,,,")

import time
from multiprocessing import Pool
import os


def Foo(i):
    time.sleep(1)
    # print("result", i)
    return f"父{os.getppid()}|子{os.getpid()},Hello print result is %s" % i


"""
pool.map()函数会将第二个参数的需要迭代的列表元素一个个的传入第一个参数我们的函数中,
"""

if __name__ == "__main__":
    with Pool(5) as pool:
        result = pool.map(
            Foo,
            ('six',
             'five',
             'three',
             'zero',
             'four',
             'seven',
             'nine',
             'eight'))
        for val in result:
            print(val)

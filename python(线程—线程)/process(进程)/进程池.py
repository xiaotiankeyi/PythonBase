from multiprocessing import Process, Pool
import time, os


def Foo(i):
    time.sleep(1)
    print("result", i)
    return "Hello print result is %s" % i


def Bas(bas):
    print(bas)


if __name__ == "__main__":
    p = Pool(5)

    result = []
    for i in range(20):
        res = p.apply_async(func=Foo, args=(i,), callback=Bas)      #异步调用
        # res = p.apply(func=Foo, args=(i,))      #同步调用
        result.append(res)


    p.close()
    p.join()

    print("end,,,,,,,")

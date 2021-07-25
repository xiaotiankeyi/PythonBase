import time
from multiprocessing import Pool


def Foo(i):
    time.sleep(1)
    print("result", i)
    return "Hello print result is %s" % i


if __name__ == "__main__":
    with Pool(5) as pool:
        result =pool.map(
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

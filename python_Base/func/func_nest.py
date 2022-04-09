"""
嵌套概念:
    函数里面在定义一层函数
"""


def max(x, y):
    return x if x > y else y


def max4(a, b, c, d):
    res1 = max(a, b)
    res2 = max(res1, c)
    res3 = max(res2, d)
    return res3


print(max4(1, 2, 3, 4))


def num(s):
    def sum(d):
        def avg(c):
            print(c)

        print(d)
        avg(6)

    print(s)
    sum(3)


num(2)

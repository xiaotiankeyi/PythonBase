from functools import reduce

def func(a):
    """
    使用内置函数reduce加lambda来实现
    :param a:
    :return:
    """
    num = reduce(lambda x, y: x * y, range(1, a + 1))
    return num

print(func(20))

def Foo(x):
    """
    使用递归函数来实现
    :param x:
    :return:
    """
    if (x == 1):
        return 1
    else:
        return x * Foo(x - 1)


print(Foo(20))

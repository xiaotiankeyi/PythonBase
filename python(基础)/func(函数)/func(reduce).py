"""
概念：
    reduce() 函数会对参数序列中元素进行累积。
    函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）
    先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
"""
num = [1, 2, 3, 5, 10]


def reduce_test(func, accept, init=None):
    if init is None:
        res = accept.pop(0)
        print(res)
    else:
        res = init
    for num in accept:
        res = func(res, num)
    return res


print(reduce_test(lambda x, y: x * y, num, 2))

"""reduce函数应用"""

from functools import reduce

"""
语法：reduce(function, iterable[, initializer])
参数：    
    function -- 函数，有两个参数
    iterable -- 可迭代对象
    initializer -- 可选，初始参数
"""
print(reduce(lambda x, y: x * y, num, 3))


def add(s, f):
    return s + f


print(reduce(add, [2, 5, 3, 8, 1, ], 2))

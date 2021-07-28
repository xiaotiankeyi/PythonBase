# 生成器
"""
概念：
    生成器是能自动实现迭代器的协议，
    举例：生成10个数字，第一个取1，第二个取2。。每个数字只能取一次。。。
    好处：可以省内存,效率高,节缩时间
    特点：yield 相当于return返回，，可以保留当前运行的转态，，想要进一步时就要__next__
"""

"""生成器表达式一"""

n = (i for i in range(10))
print(type(n))
# m = n
# print(m.__next__())
for i in n:
    print(i)


def accept():
    for i in range(10):
        yield "鸡蛋%s" % i
    print("结束")


# all = accept()
# print(all)
# print(all.__next__())
# next(all)
# next(all)

"""通过yield自定义range迭代模式"""


def frange(i, v, b):
    """生成器"""
    s = i
    while s < v:
        yield s
        s += b


d = []
for j in frange(1, 10, 0.5):
    d.append(j)

print(d)
print(type(frange))
list_a = [x for x in frange(1, 20, 0.5)]
print(list_a)

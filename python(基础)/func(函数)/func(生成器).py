"""
概念：
    生成器是能自动实现迭代器的协议，
    举例：生成10个数字，第一个取1，第二个取2。。每个数字只能取一次。。。
    好处：可以省内存,效率高
    特点：yield 相当于return返回，，可以保留当前运行的转态，，想要进一步时就要__next__
"""

"""生成器表达式"""

# n = (i for i in range(100))
# m = n
# print(m.__next__())


def accept():
    for i in range(10):
        yield "鸡蛋%s" % i
    print("结束")


# all = accept()
# print(all)
# print(all.__next__())
# next(all)
# next(all)

"""使用生成器创建新的迭代模式"""
def frange(i, v, b):
    s = i
    while s < v:
        yield s
        s += b

d = []
for j in frange(1, 10, 0.5):
    d.append(j)

print(d)

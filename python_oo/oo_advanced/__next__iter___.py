"""
    自制迭代器Iterator,
    特点:能被next访问,并不断返回下一个元素对象
    __iter__作用是可以让具备可迭代性的元素变为迭代器
"""

from collections import Iterable, Iterator

num = 100
if isinstance(num, Iterable):
    """判断num变量是不是可迭代性"""
    pass


class Foo:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        n = self.start
        self.start += 1
        return n


f = Foo(1, 5)

if isinstance(f, Iterator):
    """判断是不是迭代器"""

    print(f.__next__())
    print(f.__next__())

    # for i in Foo(1,5):
    #     print(i)


class Range:
    """简单模拟range自定义规则,加上步长"""

    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        x = self.start
        self.start += self.step
        return x


# for i in Range(1, 10, 2):
#     print(i)


class Addition:
    """自制生成器来实现自定义迭代器规则,加上yield实现"""

    def __init__(self, n, stop, step):
        self.n = n
        self.stop = stop
        self.step = step

    def handle(self):
        s = self.n
        while s < self.stop:
            yield s
            s += self.step


f1 = Addition(1, 10, 0.5)
print('返回生成器对象:', f1.handle())

for i in f1.handle():
    print(i)

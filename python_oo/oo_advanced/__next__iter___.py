"""自制迭代器"""


class Foo:
    def __init__(self, start, stop):
        self.num = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= self.stop:
            raise StopIteration
        n = self.num
        self.num += 1
        return n


f = Foo(1, 5)
# print(f.__next__())

# for i in Foo(1,5):
#     print(i)

"""简单模拟range,加上步长"""


class Range:
    def __init__(self, n, stop, step):
        self.n = n
        self.stop = stop
        self.step = step

    def __next__(self):
        if self.n >= self.stop:
            raise StopIteration
        x = self.n
        self.n += self.step
        return x

    def __iter__(self):
        return self


pass
# for i in Range(1,10,2): #
#     print(i)

"""自制迭代器规则"""


class addition:
    def __init__(self, n, stop, step):
        self.n = n
        self.stop = stop
        self.step = step

    def handle(self):
        s = self.n
        while s < self.stop:
            yield s
            s += self.step


f1 = addition(1, 10, 0.5)
for i in f1.handle():
    print(i)

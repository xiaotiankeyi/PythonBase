"""例如：第一个完全数是 6，它有约数 1、2、3、6，除去它本身 6 外，其余
3 个数相加，
1+2+3=6。第二个完全数是 28，它有约数 1、2、4、7、14、28，除去它本身 28
外，其余 5 个数相加，1+2+4+7+14=28。"""

a = []
for i in range(1, 1000):
    s = 0
    for j in range(1, i):
        if i % j == 0 and j < i:
            s += j
    if s == i:
        # print(i)
        a.append(i)
print("1000 以内完全数：%s" % a)

print(sum(range(1, 101)))

"""自制range函数"""


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


for i in Range(1, 10, 2):  #
    print(i)

r = ['s', 'd', 't', 'trt']
a = ''.join(r)
print(a)

g = [2, 4, 56, 43, 66, 43, 2, 2]
f = ''
for i in g:
    f = f + str(i)
print(f)
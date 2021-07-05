l = ['a', 'b', 'c', 'd', 'e']


def add():
    return l.pop()


x = iter(add, 'b')  # 迭代器迭代碰到"b"时就停止迭代.........
print(x.__next__())
print(x.__next__())
print(x.__next__())
# print(x.__next__())

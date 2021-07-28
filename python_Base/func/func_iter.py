# 列表具备迭代性，但不是迭代器
# iter函数可以把具备迭代性的对象转变为迭代器

l = ['a', 'b', 'c', 'd', 'e']


def add():
    return l.pop()


x = iter(add, 'b')  # 迭代器迭代碰到"b"时就停止迭代.........
print(x.__next__())
print(x.__next__())
print(x.__next__())
# print(x.__next__())

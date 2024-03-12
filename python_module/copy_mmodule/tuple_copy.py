import copy

"""
深浅拷贝的区别关键在于拷贝的对象类型是否可变
"""


tup1 = (991, "abc")
tup2 = copy.copy(tup1)  # 浅拷贝
# tup2 = tup1 # 在这个例子里浅拷贝等价于赋值

print(id(tup1))
print(id(tup2))
print(tup1 == tup2)
print(tup1 is tup2)


tup2 = copy.deepcopy(tup1)  # 深拷贝

print(id(tup1))
print(id(tup2))
print(tup1 == tup2)
print(tup1 is tup2)

"""
对于不可变对象?深拷贝还是浅拷贝都不会为我们对象建立真正的副本,
tup2和tup1的地址完全相同,实际上引用的是同一个对象
"""
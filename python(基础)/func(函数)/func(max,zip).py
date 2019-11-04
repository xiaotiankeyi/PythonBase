"""
_____zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，/
这样做的好处是节约了不少的内存。#(只支持传入序列、列表、元祖、字符串)
"""
a = [2, 4, 6]
b = [1, 5, 3, 8]
i = zip(a, b)  # 返回一个对象
print(list(i))

print(list(zip("hello", "123456")))

"""实现首尾相同"""
l = ['a', 'b', 'c', 'd', 'e', 'f']
print(list(zip(l[:-1], l[1:])))

dict = {"jack": 29, "tom": 19, "lucy": 34, "ben": 27}

print((max(dict.values())))

g = [item for item in zip(dict.keys(), dict.values())]
print('形成元祖:', g)

print('按照values最大值排序,values在前', sorted(zip(dict.values(), dict.keys(), ), reverse=True))

print('年龄最大的人:', list(max(zip(dict.values(), dict.keys()))))

"""比出最大的值。。。。"""

student = [
    {"name": "jack", "age": 23},
    {"name": "tom", "age": 33},
    {"name": "lucy", "age": 22}
]

print(max(student, key=lambda x: x["age"]))

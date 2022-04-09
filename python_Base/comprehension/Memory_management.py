# python内存管理机制:引用计数    垃圾回收   内存池机制

import sys

var1 = 'object'
var2 = var1

# id查看变量所指向那个内存地址

print('内存地址1', id(var1))
print('内存地址2', id(var2))

print(var1 is var2)

var1 = 'teacher'

print('新的内存地址1', id(var1))
print('内存地址2', id(var2))
print(var1 is var2)

a = 123456789
b = 123456789

# is判断两个对象所引用地址是否是同一个地址
print('判断变量a,b内存地址', a is b)

# 长短字符串处理逻辑不一样
c = 'hello'
d = 'hello'
print('判断两个短字符串变量c,d', c is d)

e = 'hello world i`am is jack'
f = 'hello world i`am is jack'
print('判断两个长字符串变量e,f', e is f)

# 列表
g = []
h = []
print('判断两个列表变量g,h', g is h)

# 引用计数
print("-" * 50)
print("查看列表g的引用计数", sys.getrefcount(g))

# 引用计数增加
print(sys.getrefcount(123))
i = 123
print(sys.getrefcount(123))

if __name__ == "__main__":
    pass

# 浅拷贝深拷贝
# 浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
# 深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。

import copy

# 变量赋值
a = 'hello'
b = a
print(id(a), id(b))

# 浅拷贝实例
print('浅拷贝实例')
c = {'a':[2, 3, 4, 23, 56]}

d = copy.copy(c)
print(id(c), c)
print(id(d), d)

c['a'].append('jack')
print(id(c), c)
print(id(d), d)


# 深拷贝实例
print('深拷贝实例')
g = {'a':[2, 3, 4, 23, 56]}
y = copy.deepcopy(g)
print(id(g), g)
print(id(y), y)

g['a'].append('jack')
print(id(g), g)
print(id(y), y)
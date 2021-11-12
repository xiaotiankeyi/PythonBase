# 浅拷贝深拷贝
# 浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
# 深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。

import copy

# 变量赋值
a = 'hello'
b = a
print('赋值', id(a), id(b))

# 浅拷贝实例
print('浅拷贝实例'+'-'*50)
# 浅拷贝是在另一块地址中创建一个新的变量或容器，但是容器内的元素的地址均是源对象的元素的地址的拷贝。
# 也就是说新的容器中指向了旧的元素（ 新瓶装旧酒 ）。

c = [2, 3, 4, 23, 56, ['name', 'age']]      #原对象原元素

d = copy.copy(c)
print(id(c), c)
print(id(d), d)

print("# 对原对象增加了新的元素")
c.append(100)
print(id(c), c)
print(id(d), d)

print("# 对原对象里的原元素进行修改")
c[5].append("gander")
print(id(c), c)
print(id(d), d)


# 深拷贝实例
print('深拷贝实例'+'-'*50)
# '深拷贝实例, y完全拷贝了g的父对象及其子对象，两者是完全独立的'
g = {'a':[2, 3, 4, 23, 56]}
y = copy.deepcopy(g)
print(id(g), g)
print(id(y), y)

g['a'].append('jack')
y['b'] = 34
print(id(g), g)
print(id(y), y)
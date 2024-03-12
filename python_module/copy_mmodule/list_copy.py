import copy

lis1 = [991, "abc", (9, 993), [994, 995], [888, 887], {
    "name": "Tom"}, (996, [997, 998]), (888, (886, 886))]
lis2 = copy.copy(lis1)  # 浅拷贝

print(id(lis1))
print(id(lis2))

print(lis1 == lis2)
print(lis1 is lis2)

# 往list2中新添加一个元素,查看list1变化,结论新增加的元素不在list1中显示
lis2.append("test")
print("查看1:", lis1)
print("查看2:", lis2)
print(lis1[0] is lis2[0])

# 修改list2中的元素,查看list1变化,结论原对象list1也发生变化
lis2[3].append("jack")
print("查看1:", lis1)
print("查看2:", lis2)

lis2 = copy.deepcopy(lis1)  # 深拷贝
print(id(lis1))
print(id(lis2))

print(lis1 == lis2)
print(lis1 is lis2)
print(lis1[0] is lis2[0])
"""
对于可变对象来说?深拷贝和浅拷贝都会开辟新地址?完成对象的拷贝
"""
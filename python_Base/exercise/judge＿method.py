"""判断是否为空的三种方法
在python中 None, False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False
"""
"""
在python中not是逻辑判断词,用于布尔型True和False,not True为False,not False为True,以下是几个常用的not的用法
    not与逻辑判断句if连用,代表not后面的表达式为False的时候,执行冒号后面的语句
"""

a = []
print(not a)

c = not a
print('c为:', c)
print(None is not None)  # 判断None is不等于None

print(a is None)


if not a:
    print('为None')  # 解释
else:
    print('不为None')

"""
if a not in b,a是元素,b是列表或字典,这句话的意思是如果a不在列表b中,那么就执行冒号后面的语句
"""
a = [3, 4, 5]
if 7 not in a:
    print('执行')

j = None
if j is not None:
    print('是')
else:
    print('不是')

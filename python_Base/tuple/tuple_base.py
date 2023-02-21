"""
不支持修改,为不可变类型
不支持删除单个元素
有序结构,可存储不同结构类型数据
max,min,len
支持切片访问,循环操作
可以最为dict的键
"""
my_tuple = ('name', 'age', 'sex', (23, 5, 1, 6, 54),
            [
                2, 43, 11, 'linux', 'phone'
],
    'request', 'response', {'paras': 'split', 'str': 'replace'})
print(my_tuple[3][2])
print(my_tuple[::-1])
print(my_tuple[1:6])
for reception in my_tuple:
    print(reception)
print(len(my_tuple))
print('name' in my_tuple)

for reception in my_tuple:
    print(reception)
print(len(my_tuple))
print('name' in my_tuple)
print(my_tuple.index('request'))
print((my_tuple.count('response')))

for i in range(len(my_tuple)):
    print(i, my_tuple[i])

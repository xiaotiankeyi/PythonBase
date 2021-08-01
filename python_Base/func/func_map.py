"""
概念：map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
如下：定义好每个数字加1的功能.....
"""


def addition(i):
    return i + 1


def map_test(func, array):
    ret = []
    for i in array:
        res = func(i)
        ret.append(res)
    return ret


li = [2, 4, 6, 8, 10, 12]
paras = map_test(addition, li)
print(paras)


"""......第二种使用lambda表达式....."""
accept = map_test(lambda i: i + 1, li)
print(accept)

"""....第三种.....系统提供的内置函数map"""
use = map(lambda i: i + 1, li)

print(list(use))
update = map(addition, li)
print(list(update))

value = map(lambda x,y: x+y, li, li)
print(list(value))

# 当逻辑复杂时不建议用lambda
# 传入的必须是可for循环的对象、如列表、字符串、字典


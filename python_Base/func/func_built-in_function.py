# 内置函数built-in function
# _______abs()______返回数字的绝对值
import math
print(abs(23))

# _______enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列,同时列出数据和数据下标,一般用在
# for 循环当中,
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for total, i in enumerate(seasons):
    print(total, i)

# ______eval() 函数用来执行一个字符串表达式,并返回表达式的值,(把字符串中的数据结构给提取出来,,,,)
paras = "{'name':'jack'}"
accept = eval(paras)
print(accept)
n = eval("3 * 4")
print(n)

# ______pow() 方法返回 xy（x的y次方） 的值,,,计算x值得平方

print("math.pow(100, 2)", math.pow(100, 2))
# 内置用法
print("pow(23, 2)", pow(23, 2))
# 函数是计算x的y次方,如果z在存在,则再对结果进行取模,其结果等效于pow(x,y) %z
print("pow(23, 2[, z])", pow(23, 2) % 1)

# ______sum() 方法对系列进行求和计算,
print(sum([2, 5, 6]))
print(sum([2, 5, 6], 2))
print(sum((5, 7, 9)))
print(sum((5, 7, 9), 2))


# _____issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类,
class A:
    pass


class B(A):
    pass


# 判断B是不是A的子类
print(issubclass(B, A))  # 返回 True

"""______filter() 函数用于过滤序列,过滤掉不符合条件的元素,返回一个迭代器对象,如果要转换为列表,可以使用 list() 来转换,
该接收两个参数,第一个为函数,第二个为序列,序列的每个元素作为参数传递给函数进行判,然后返回 True 或 False,最后将返回 True 的元素放到新列表中,"""


def is_odd(n):
    return n % 2 == 1


tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
new_list = list(tmplist)
print(new_list)

# ______chr() 用一个范围在 range（256）内的（就是0～255）整数作参数,返回一个对应的字符,
print(chr(71))


# ______callable() 函数用于检查一个对象是否是可调用的,如果返回 True,object 仍然可能调用失败；但如果返回
# False,调用对象 object 绝对不会成功,
def sum(a, b):
    return a + b


print(callable(sum))

# ______format()字符串格式化、基本语法是通过 {} 和 : 来代替以前的 % ,
print("{} {}".format("hello", "world"))  # 不指定位置,默认顺序
print("{0} {1}".format("hello", "world"))  # 设置指定位置
print("{1} {2} {1}".format("hello", "world", "hi"))  # 设置指定位置
# 设置参数
print("网站名:{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
# 通过字典设置参数......
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名:{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名:{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

# _____frozenset() 返回一个冻结的集合,冻结后集合不能再添加或删除任何元素,
frozenset([3, 6, 2, 15, 6, 43, 1])

# _____map() 会根据提供的函数对指定序列做映射,
map(lambda x: x ** 2, [1, 2, 3, 4, 5])

# _____max() 方法返回给定参数的最大值,参数可以为序列,
print("max(20,56,21,78)", max(20, 56, 21, 78))
dict = {'alex': 12, 'jack': 20}
print(max(zip(dict.values(), dict.keys())))

# _____zip() 函数用于将可迭代的对象作为参数,将对象中对应的元素打包成一个个元组,然后返回由这些元组组成的对象,这样做的好处是节约了不少的内存,
a = [2, 4, 6]  # (只支持传入序列、列表、元祖、字符串)
b = [1, 5, 3]
zipped = zip(a, b)
zipped = list(zipped)
print(zipped)

# _____hash() 用于获取取一个对象（字符串或者数值等）的哈希值,
print(hash('test'))
print(hash(23))

# ____min() 方法返回给定参数的最小值,参数可以为序列,
print("min(4,2,6,3,)", min(4, 2, 6, 3))
print("min(-20, 100, 400) : ", min(-20, 100, 400))

# _____set() 函数创建一个无序不重复元素集,可进行关系测试,删除重复数据,还可以计算交集、差集、并集等,
y = ('google')
print(set(y))


# _____delattr 函数用于删除属性,delattr(x, 'foobar') 相等于 del x.foobar,
class Collection():
    x = 10
    y = -5
    z = 0


delattr(Collection, 'z')

# _____help() 函数用于查看函数或模块用途的详细说明,
# help('str')

# _____next() 返回迭代器的下一个项目,


# _____id() 函数用于获取对象的内存地址,
name = 'jack'
print(id(name))

# _____sorted() 函数对所有可迭代的对象进行排序操作,
a = [2, 6, 3, 7, 2, 1, 9]
b = sorted(a)
print(b)
people = [
    {'name': 'alex', 'age': 23},
    {'name': 'jack', 'age': 67},
    {'name': 'tom', 'age': 34}
]
print(sorted(people, key=lambda dict: dict['age'], reverse=True))

# ____bytes____
name = '你好'
print(bytes(name, encoding="utf8"))  # 转化为二进制

# ____decode____
name = '你好'
print(bytes(name, encoding="utf8").decode("utf8"))  # 解码

# ____divmod____分页功能,(10,3)总共10条记录,每页有3条
print(divmod(10, 3))

print(ord("r"))

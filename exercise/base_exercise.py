"""x 的 y 次方(xy) 以下表达式"""
v = 3 ** 2
print(v)

"""3*1**3表达式输出结果"""
b = 3 * 1 ** 3  # 正确的是 3。** 拥有更高的优先级。
print(b)

"""9//2表达式输出为,取整除,返回商的整数部分"""
s = 9 // 2
print(s)

"""如果表达式的操作符有相同的优先级，则运算规则是？____从左到右"""
g = (3 + 1) * (5 + 5)
print(g)

"""以下代码输出为"""
x = True
y = False
z = False

if x or y and z:  # 这里先运算and,y等于0,返回y的值False,在运算or,x不是0,返回x的值True
    print("yes")
else:
    print("no")

"""在bool值中代表False的有(0),([]),({}),(None),(()) """
v = ()
print(bool(v))

"""以下代码输出为"""
x = False
y = True
z = True

if x or y and z:  # 这里先运算and,y不等于0,返回z的值True,在运算or,x等于0返回y的值True
    print("yes")
else:
    print("no")

"""逻辑运算符的优先级顺序为(not, and, or)"""
x = True
y = False
z = False
print(not x or y)  # x不为零,先返回True,在反转为False
if not x or y:
    print(not x or y)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)

"""or逻辑运算符例题"""
a = 0
c = 10
print((a or c))

""""""
i = sum = 0

while i <= 4:
    sum += i
    i = i + 1

# print(sum)

"""函数递归"""


def Foo(x):
    print(x)
    if (x == 1):
        return 1
    else:
        return x + Foo(x - 1)

# print(Foo(4))

a = [2, 5, -1,56,3, 2, -4, -23]
b = [i for i in a if int(i) >=1 ]
print('大于1的数有{}个'.format(len(b)))
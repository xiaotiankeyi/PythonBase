
str = 'hello world smartable application'
# print(len(str))
# 计算那个单词最长

dictionary = {}

a = 0
for i in str:
    # print(i)
    if i == " ":
        a = 0
        continue
    a += 1

print(a)

# 记录当前长度
c = 0
# 记录历史长度
b = 0
for i in str:
    # print(i)
    if i == " ":
        c = 0
        continue
    c += 1
    if c > b:
        b = c

# print(b)

# 统计每个单词的长度方法一
# 记录当前长度
c = 0
d = ""
f = 0
dictionary = {}
for i in str:
    # print(i)
    if i == " ":
        dictionary[d] = c
        d = ""
        c = 0
        f += 1
        continue
    d += i
    c += 1
    f += 1
    if f == len(str):
        dictionary[d] = c

# print(dictionary)
# 统计每个单词的长度方法二

d = ""
f = 0
dictionary = {}
for i, v in enumerate(str, 1):
    # print(i, v)
    if v == " ":
        dictionary[d] = len(d)
        d = ""
        c = 0
        continue
    d += v
    if int(i) == len(str):
        dictionary[d] = len(d)

# print(dictionary)

# 判断是不是质数
"""
num = int(input('请输入一个数字:'))
if num > 1:
    for i in range(2, num):
        print(i)
        if (num % i) == 0:
            print(num, "不是质数")
            print(i, "乘于", num // i, "是", num)
            break
    else:
        print(num, "是质数")
else:
    print('不是质数,')


# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
"""


def fanzhuan(list):
    """实现反转"""
    a = []
    i = len(list)
    while i > 0:
        a.append(list[i - 1])  # 生成一个新的列表,原列表的最后一位成为第一位
        i -= 1  # 依次向前进一位
    return a


fa = fanzhuan([34, 12, 54, 234, 65, 122])
print(fa)
if __name__ == "__main__":
    pass

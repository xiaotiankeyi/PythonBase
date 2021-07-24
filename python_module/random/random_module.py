from random import randint
import random

# v = random.random()
# print(v)
#
# n = random.randint(0, 3)
# print(n)
#
# m = random.randrange(1, 4)
# print(m)
#
# """概率出现"""
# g = random.choice([2, 4, 256, ])
# print(g)
#
# """顺序打乱"""
# h = [3, 45, 8, 6, 34, 56, 5]
# random.shuffle(h)
# print(h)

"""随机验证码"""


def check_code():
    checkcode = ''
    for i in range(5):
        current = random.randint(0, 5)
        if current != i:
            temp = chr(random.randint(65, 90))
        else:
            temp = random.randint(0, 9)
        checkcode += str(temp)
    return checkcode


# b = check_code()
# print(b)


def make_code(n):
    res = ''
    for i in range(n):
        s1 = chr(randint(65, 90))
        s2 = str(randint(1, 9))
        res += random.choice([s1, s2])
    return res

# print(make_code(4))

# print(chr(90))


'''指定随机生成11位数'''
j = 10
id = ''.join(str(i) for i in random.sample(range(0, 11), j))

"""随机生成字符串"""
string = ''.join(i for i in random.sample(
    'zyxwvutsrqponmlkjihgfedcbaABCDEFGHIJKLMNOPQRSTUVWX', 5))
print(string)

parameter = ''.join(str(i)
                    for i in random.sample(range(0, 11), 10)) + '@qq.com'
print(parameter)

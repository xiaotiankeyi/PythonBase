# _____int____字符串的转换,,,将字符串转换为数字
parameter = '123'
number = int(parameter)
print(number)

# ____type()___看看是什么数字类型
print(type(number), number)

# ____bit_length____当前数字的二进制,至少用几位来表示
age = 2121
num = age.bit_length()
print(num)


"""求质数"""

def handle():
    l = []
    for i in range(2, 101):
        # print(i)
        flag = 0
        for j in range(2, i - 1):
            # print(j)
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            l.append(i)
        print(i)


"""菲波那切数列"""

def fid(n):
    a = 0
    b = 1
    while a <= n:
        print(a, end="", flush=True)
        a, b = b, a + b
    return ''
# print(fid(100))


def fib_loop(n):
    # a, b = 0, 1
    # for i in range(n + 1):
    #   a, b = b, a + b
    # return a
    """递归函数"""
    if n <= 1:
        return n
    else:
        return (fib_loop(n -1) + fib_loop(n-2))


for i in range(10):
    print(fib_loop(i), end=' ')

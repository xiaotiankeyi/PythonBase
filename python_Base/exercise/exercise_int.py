'''
定义 multiple 函数,传可变参数（该参数全为float）,return 所有可变参数相乘的积,无参数则返回 None；
如:multiple(3,2) return 6；multiple(3.5,2) return 7.0；multiple(3.5,2,3) return 21.0；multiple(3,2,0,3,) return 0；
'''


def multiple(*num):
    # 定于一个变量来接收结果
    n = 1
    if len(num) == 0:
        return None
    else:
        for i in range(len(num)):
            # 第一次(n=1*3),第二次(n=3*3)
            n = n * num[i]
        return n


# print(multiple(3, 5))

"""实现一个判断用户输入的年份是否是闰年的程序......."""


def judge():
    while True:
        year = int(input("请输入年份>>>>>>   ").strip())
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            print("%s it is ruinian" % year)
            break
        else:
            print("%s not ruinian" % year)
            break


# judge()

"""九九乘法表"""


def count():
    for i in range(1, 10):
        for x in range(1, i + 1):
            print("%d * %d = %d\t" % (x, i, i * x), end="")
        print("")


# count()

"""求100至300之间的素数......"""


def computer():
    a = []
    for n in range(100, 301):
        count = 0
        for x in range(2, n - 1):
            if n % x == 0:
                count += 1
        if count == 0:
            a.append(n)
    print(a)


"""请找到列表中任意两个元素相加能够等于9的元素集合,列[(2,7), (1,8)]"""


def add():
    nums = [2, 7, 11, 15, 1, 8, 7]
    total = []
    for i in nums:
        for f in nums:
            if i + f == 9:
                d = list((i, f))
                d.sort()
                b = tuple(d)
                if b not in total:
                    total.append(b)


add()

"""公鸡5文钱一只,母鸡3文钱一只,小鸡3只一文钱,用100文钱买100只鸡,其中 公鸡,母鸡,
小鸡都必须要有,问公鸡,母鸡,小鸡要买多少只刚好凑足100文钱?"""


def avg():
    li = []
    for i in range(1, 100 // 5):
        for x in range(1, 100 // 3):
            for c in range(1, 100 * 3):
                if i + x + c == 100 and i * 5 + x * 3 + c / 3 == 100:
                    print(i, x, c)


avg()


def sum():
    distance = int(input("请输入计算的数字>>>>>>> ").strip())
    if distance > 32:
        km = distance - 32
        if km % 20 == 0:
            print((6 + km / 20) * 0.8)
        else:
            print((6 + (km / 20) + 1) * 0.8)
    else:
        print(distance)


sum()

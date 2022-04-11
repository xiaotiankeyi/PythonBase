"""
函数的递归操作...........
    概念:
        必须要有明确的结束条件,,,
    函数尾递归优化:
        在函数最后一步进入下一层(最后一步不代表最后一行)
"""

"""直接调用本身"""




from time import sleep
def fi():
    print("from f1")
    fi()


# fi()

"""间接调用本身"""


def f1():
    print("from f1")
    f2()


def f2():
    print("from f2")
    f1()


# f2()

"""例一"""
"""
实现:10 / 2 = 5 | 5 / 2 = 2 | 2 / 2 = 1 |
"""


def salary(n):
    print(n)
    """递归终止条件.....当n除于2整数位等于0时结束"""
    if int(n / 2) == 0:
        return n
    res = salary(int(n / 2))
    return res


# res = salary(10)
# print(res)

"""例二"""

person_list = ['Tom', 'alex', 'lucy', 'jack', 'zsc']


def ask_way(person_list):
    print('-' * 60)
    if len(person_list) == 0:
        return '根本没人知道'
    person = person_list.pop(0)
    if person == 'jack':
        return '%s说:我知道,老男孩就在沙河汇德商厦,下地铁就是' % person

    print('hi 美男[%s],敢问路在何方' % person)
    print('%s回答道:我不知道,但念你慧眼识猪,你等着,我帮你问问%s...' % (person, person_list))
    sleep(3)
    res = ask_way(person_list)

    print('%s问的结果是: %res' % (person, res))
    return res


# res = ask_way(person_list)
# print(res)


"""实现阶乘"""


def num(n):
    if n == 1:
        return 1
    return n * num(n - 1)


m = num(8)
print(m)
"""猴子吃桃案例"""
s = 1


def func(x): return (x + 1) * 2


for i in range(9):
    s = func(s)


# print(s)

# 定义一个类(num是需要给出的参数)
# 一定要有临界值
# 要有递推的关系
def digui(num):
    # 打印num
    print('$' + str(num))

    # 如果num大于0
    if num > 0:
        # 调用自己每次在减一
        digui(num - 1)
    # 否则
    else:
        # 打印*20次(用来分割线)
        print("*" * 20)

    # 打印num
    print('$' + str(num))


# digui(3)

"""以上的原理是输入3 打印3 判断3是否大于0 符合调用自己-1 得到2 2继续当参数传上去 打印2 判断2是否大于0 符合调用自己-1以此类推
不满足的情况下打印分隔符 然后把上面的得到结果数据 打印出来"""

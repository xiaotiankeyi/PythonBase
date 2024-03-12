'''把列表里面的元素转换为字符串___多种元素的情况下
用for循环.....'''


def select():
    my_list = [12, 45, 677, 323, 'jack', 'Tom', 'alex']
    s = " "
    for i in my_list:
        s = s + str(i)
    print(s)


select()

"""_____如果只有字符串........"""


def string():
    an_list = ['qwe', 'weq', 'pre']
    v = "".join(an_list)
    print(v)


string()

"""
定义 purify 函数,传一 list 参数;去除该 list 中所有的偶数(该list中全为int元素)
如: purify([3,1,5,2,6,1,4])  会 return [2,6,4]
"""


def purify(parameter):
    # 转化为list列表
    num = list(parameter)
    # print(num)
    # 添加一个列表来接收
    reception = []
    # 对列表进行循环
    for count in range(len(num)):
        # 进行数据类型转换
        avg = int(num[count])
        if avg % 2 == 0:
            reception.append(avg)
    return reception


value = purify("619347420842")
print(value)
"""1. 有列表data=['alex',49,[1900,3,18]],分别取出列表中的名字,年龄,出生的年,月,日赋值给不同的变量"""


def values():
    data = ['alex', 49, [1900, 3, 18]]
    accept = {}
    for paras in range(len(data)):
        accept.update({"name": data[0], "age": data[1], "birthday": data[2]})

    print(accept)


values()


def handle(a, li=['1']):
    # 测试传递可表参数
    li = []
    li.append(a)
    return li

print(handle(2))
print(handle(3))
print(handle(4))
print(handle('a', li=['b']))
print(handle(5))

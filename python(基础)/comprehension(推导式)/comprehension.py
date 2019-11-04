"""创建一个列表，往里面添加10个元素"""


def create():
    li = []
    for i in range(1, 10):
        li.append(i * 2)
    print(li)
    """列表推导式的表达方式"""
    list = [i * 2 for i in range(1, 10)]
    print(list)

    """计算乘积,取模并大于100的数"""
    total = []
    for i in range(1, 10):
        for x in range(10, 20):
            if (i * x) % 2 == 0 and (i * x) > 100:
                total.append(i * x)
    print(total)
    """列表推导式的表达式方式"""
    count = [i * x for i in range(1, 10) for x in range(10, 20) if (i * x) % 2 == 0 and (i * x) > 100]
    print(count)


# create()


def dictionary():
    """key为迭代出来的数,values值为key+1"""
    dict_1 = {}
    for f in range(1, 5):
        dict_1[f] = f + 1
    print(dict_1)
    """字典推导式表达方式"""
    dict = {i: i + 1 for i in range(1, 5)}
    print(dict)

    """用zip拼接字典,key值有迭代器生成,values为自定义"""
    order_by = "abcdefg"
    group_by = {}
    for i, v in zip(range(1, 6), order_by):
        group_by[i] = v
    print(group_by)

    """字典推导式"""
    group = {i: v for i, v in zip(range(1, 6), 'abcdefg')}
    print(group)


dictionary()

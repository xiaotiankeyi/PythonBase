"""写函数,计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数"""

def count(accept):
    num = list(accept)
    sum = 0
    for total in range(len(num)):
        sum += total
    return sum


"""写函数,判断用户传入的对象(字符串、列表、元组)长度是否大于10,,,并计算出个数"""


def extent(accept):
    string = accept
    if len(string) > 10:
        sum = 0
        for total in range(len(string)):
            sum += total
        return "succeed", sum
    else:
        return "fail"


# print(extent("djiascasfe,['strip','split'],('lowe','upper')"))


# 第二种
def check_str(msg):
    res = {
        'num': 0,
        'string': 0,
        'space': 0,
        'other': 0,
    }
    for s in msg:
        if s.isdigit():
            res['num'] += 1
        elif s.isalpha():
            res['string'] += 1
        elif s.isspace():
            res['space'] += 1
        else:
            res['other'] += 1
    return res


# res=check_str('hello name:aSB passowrd:alex3714')
# print(res)

"""写函数,检查用户传入的对象(字符串、列表、元组)的每一个元素是否含有空内容,"""


def examine(paras):
    print(type(paras))
    if paras is not None:
        return "have"
    else:
        return "none"


# print(examine(["name","alex","lucy"," "," "]))

"""写函数,检查传入列表的长度,如果大于2,那么仅保留前两个长度的内容,并将新内容返回给调用者,"""


def num(accept):
    if len(accept) > 2:
        del accept[2:]
        return accept


# print(num([32,34,121,5,6,65,]))

"""写函数,检查获取传入列表或元组对象的所有奇数位索引对应的元素,并将其作为新列表返回给调用者,"""


def accept(paras, *args, **kwargs):
    li = []
    for num in range(len(paras)):
        if paras[num] % 2 == 0:
            li.append(paras[num])
            # li.append(num)
            # li.append("<>")
        else:
            pass
    return li


# print(accept([3,4,1,6,9,0,32,54,12,78,12]))
# 第二种
def func2(seq):
    return seq[::2]


# print(func2([1, 2, 3, 4, 5, 6, 7]))

"""写函数,检查传入字典的每一个value的长度,如果大于2,那么仅保留前两个长度的内容,并将新内容返回给调用者,"""


def dict(a, **kwargs):
    new = {}
    for k, y in a.items():
        if len(y) > 2:
            new[k] = y[0:2]
        else:
            new[k] = y
    return new


dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
# paras = dict(dic)
# print(paras)

"""写函数,利用递归获取斐波那契数列中的第 10 个数,并将该值返回给调用者,"""


def f1(a, a1, a2):
    print(a, a1, a2)
    if a == 10:
        return a1
    a3 = a1 + a2
    r = f1(a + 1, a2, a3)
    return r
# ret = f1(1,0,1)
# print(ret)


"""将names=['egon','alex_sb','wupeiqi','yuanhao']中的名字全部变大写"""

names = ['egon', 'alex_sb', 'wupeiqi', 'yuanhao']
li_1 = [i.upper() for i in names]
# print(li_1)


def handle(paras):
    user = []
    for i in paras:
        i = i.upper()
        user.append(i)
        # print(i)
    return user

# v = handle(names)
# print(v)


"""将names=['egon','alex_sb','wupeiqi','yuanhao']中以sb结尾的名字过滤掉,然后用字典保存剩下的名字和 长度"""
name_1 = ['egon', 'alex_sb', 'wupeiqi', 'yuanhao']
li = [len(i) for i in name_1 if not i.endswith("sd")]


def create(paras):
    quest = []
    for n in paras:
        if not n.endswith("sb"):
            quest.append(n)
        dic = {i: len(i) for i in quest}
        # if not n.endswith("sb"):
        #     quest.append(len(n))
    return dic

# f = create(name_1)
# print(f)


def handle_1():
    g = ['EGON', 'ALEX_SB', 'WUPEIQI', 'YUANHAO']
    dic_1 = {i: len(i) for i in g}
    h = {}
    for i in g:
        # print(i,count(i))
        h[i] = len(i)
    return h

if __name__ == "__main__":
    print(count("12132121"))

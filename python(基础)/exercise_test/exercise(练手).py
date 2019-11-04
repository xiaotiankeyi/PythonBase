import re


def handle():
    """
    一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
    　　　第10次落地时，共经过多少米？第10次反弹多高？
    """
    sn = 100
    Hn = sn / 2
    for n in range(2, 11):
        sn += 2 * Hn
        Hn /= 2
    print("Total of road is %f " % sn)
    print("The tenth is %f meter" % Hn)


def accept():
    student = [{"name": "jack", "age": 23, "sex": "男"}]

    result = "\t序号\t姓名\t年龄\t性别"
    """ 定义序号"""
    for i, n in enumerate(student):
        number = i
        result = "\t序号\t姓名\t年龄\t性别"
        print(result)
        result2 = number, "\t%s\t%s\t%s" % (n["name"], n["age"], n["sex"])
        print(i, n)


def response(n):
    """定义 scrabble_score 函数，传一 str 参数。预设一组词典（见下方引用），根据词典中字母对应的数值，\
    将传入参数的每个字母数值相加（非字母不加，注意大小写转换）；如："Word !"  分别对应取 "w": 4 , "o": 1, "r": 1,"d": 2，
     相加为 4+1+1+2 = 8  return 该值 """
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1,
             "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}

    n = list(n)
    count = 0
    for i in range(len(n)):
        v = n[i].lower()
        if v in score.keys():
            count += score[v]
            print(score[v])  # 取出相加的数
    return count


# b = response('ajdan')
# print(b)


def censor(s, h='new'):
    """ 定义 censor 函数，传两个 str 参数：s, h；若 s 字符串中的单词包含 h（全小写）时
    （不区分大小写，暂时仅考虑空格分隔的单词），将其隐藏，每个隐藏的字母显示为 *；该方法为不完善的隐藏字符方法，
    如隐藏字符后有标点，则仍会显示。"""
    if h in s:
        f =s.replace(h, '***')   #用字符串方式替换
        f = re.sub(h, '*', s)  # 用正则表达式替换
    return f


# g = censor('new hello new')
# print(g)

def repetition(paras):
    """去重操作"""
    g = []
    for t in paras:
        if t not in g:
            g.append(t)
    # v = list(set(paras))  #但是排序被改变
    return g


d = [2,4,25,6,4,7,32,1,1,9]
# h = repetition(d)
# print(h)


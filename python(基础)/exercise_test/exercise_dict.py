'''
取字典score中values的值，，在进行累加..........
'''
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8,
         "z": 10}


def sum():
    lists = []
    for value in score.values():  # 用values去values值......
        lists.append(value)  # 添加到列表中
    print(lists)
    i = 0  # 设置变量(i)来接收.......
    for num in lists:  # 设置循环遍历列表......
        # print(num, lists[num])
        i += num
    print(i)


sum()  # 调用函数


def paras(s):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8,
             "z": 10}
    f = list(s)  # 把输入的字符串转化为list列表
    num = 0
    for total in range(len(f)):  # 循环出list列表中的索引
        letter = f[total].lower()  # 把每个索引对应的字符转化为小写
        if letter in score.keys():  # 让变量letter在列表score里面匹配
            print(letter, score[letter])  # 显示相加的(字母)和对应的(values)
            num += score[letter]
    return num


n = paras("spqncr")
print(n)

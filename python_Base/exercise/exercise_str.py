'''关于字符串方法的操作.....'''


def strip():
    params = input('请输入一个参数>>>>>')

    if params.isalnum():
        print('你输入的是一个数字+字母字符串.......')
    else:
        print('请输入纯数字.......')


'''输入一个参数，计算出索引和显示出索引对应的字符'''


def splat():
    test = input(">>>>>")
    for item in range(0, len(test)):
        print(item, test[item])


"""开发敏感过滤器。。出现敏感词汇后替换成*****显示"""


def character():
    i = '一本道'
    parameter = input('输入内容>>>>>')
    if parameter in i:
        e = parameter.replace('一本道', '****')
        print(e)
    else:
        print(parameter)


"""制作随机验证码........"""


def check_code():
    import random
    checkcode = ''
    for i in range(4):
        current = random.randint(0, 4)
        if current != i:
            temp = chr(random.randint(65, 90))
        else:
            temp = random.randint(0, 9)
        checkcode += str(temp)
    return checkcode


while True:
    code = check_code()
    print(code)
    verify = input('请输入验证码>>>')
    if verify.upper() == code:
        print('succeed')
        break

"""制作表格"""


def tables():
    s = ''
    while True:
        v1 = input(">>>>")
        v2 = input(">>>>")
        v3 = input(">>>>")
        template = "{0}\t{1}\t{2}\n"
        v = template.format(v1, v2, v3)
        s = s + v
        if v1 == "q":
            break
    print(s.expandtabs(20))


'''
分页显示内容:
        a.通过for循环创建301条数据,数据类型不限。。。如
            alex1   alex1@163.com   pad1
        b.提示用户输入页面,在显示输入页面的内容......
        (每一页只显示10条内容)
'''


def group():
    paras = []
    for i in range(0, 301):
        dictionary = {
            "name": "alex" +
            str(i),
            "e_mail": "alex" +
            str(i) +
            "@163.com",
            "pad" +
            str(i): "123"}
        paras.append(dictionary)
    print(paras)

    num = int(input("请输入页码>>>>"))
    start = (num - 1) * 10
    end = num * 10
    result = paras[start:end]
    for item in result:
        # items = "=".join(item)
        item = str(item)
        print(item.replace(":", "="), type(item))


"""2 统计s='hello alex alex say hello sb sb'中每个单词的个数,结果如：{'hello': 2, 'alex': 2, 'say': 1, 'sb': 2}"""


def stop():
    s = "hello alex alex say hello sb sb"
    s = s.split(' ')
    collect = {}
    for accept in s:
        if accept in collect:
            collect[accept] += 1
        else:
            collect[accept] = 1
    print(collect)

def file_test(name, clean_msg):
    desktop_path = "C:/Users/Public/Desktop/"
    full_path = desktop_path + name + ".txt"
    file = open(full_path, "a+")
    file.write(clean_msg)
    file.close()
    # print(file.name)
    print('Done')


# file_test('python', "hello, word")

"""过滤条件"""


def test_filter(word, censored_word='lan', changer='******', ):
    return word.replace(censored_word, changer)


# n = test_filter('python is lan')
# print(n)

"""实现文本过滤"""


def collect(name, msg):
    clean_msg = test_filter(msg)    #调用过滤条件,
    file_test(name, clean_msg)


# collect("python", "python is lan and lan or lan" )


"""读取指定路径的文件...."""


def seek(file, ):
    with open("C:/Users/Public/Desktop/" + file, 'r') as d:
        print(d.name)
        print(d.read())


# seek("python.txt")

"""在桌面上创建10个文件"""


def create_file(name, msg):
    num = 0
    while num < 10:
        desktop_path = "C:/Users/Public/Desktop/"
        full_path = desktop_path + name + str(num) + ".txt"
        file = open(full_path, "w+")
        file.write(msg)
        file.close()
        num += 1
    print('Done')


# create_file("python", "循环创建10个文件.....")

""".....查询指定的字符串在文章中出现的次数，并按大小排序.........."""


def sum():
    with open("C:/Users/Public/Desktop/python.txt", "r", encoding='utf8') as a:
        collection = []
        for rad_word in a.read().split():
            collection.append(rad_word.lower())
        print(collection)

    paras = ['on', 'the', 'in', 'of', 'i']
    dict = {}
    for i in paras:
        dict[i] = collection.count(i)
    print(dict)

    for k, y in dict.items():
        pass
    """排序"""
    print('按照出现次数排序', sorted(zip(dict.values(), dict.keys(), ), reverse=True))

    print('按照出现次数排序,显示其key', sorted(dict, key=lambda key: dict[key], reverse=True))

    for word in sorted(dict, key=lambda x: dict[x], reverse=True):
        print("{} -- {} times".format(word, dict[word]))


# sum()

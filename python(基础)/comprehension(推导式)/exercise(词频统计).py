import string

path = "Walden.txt"

with open(path, 'r+', encoding='utf8') as f:
    words = [rad_word.strip(string.punctuation).lower()
             for rad_word in f.read().split()]
    """转化为集合去重复操作"""
    words_index = set(words)

    """列表单词为key，出现次数为values"""
    count_dict = {index: words.count(index) for index in words_index}
    """上面的字典推导式表现形式为...."""
    # dict = {}
    # for i in words_index:
    #     for index in words_index:
    #         dict[index] = words.count(index)
    #     print(dict)
    #     break
    print(count_dict)
"""排序"""
for word in sorted(count_dict, key=lambda x: count_dict[x], reverse=True):
    # print("{} -- {} times".format(word, count_dict[word]))
    pass

"""自定义查找......"""


def Sum():
    with open("Walden.txt", "r", encoding='utf8') as a:
        collection = []
        for rad_word in a.read().split():
            collection.append(rad_word.lower())
        print(collection)

    """列表单词为key，出现次数为values"""
    dict = {}
    for i in collection:
        dict[i] = collection.count(i)
    print(dict)

    # for k, y in dict.items():
    #     pass
    """排序"""
    print(sorted(zip(dict.values(), dict.keys(),), reverse=True))
    # print(sorted(dict, key=lambda key: dict[key], reverse=True))
    for word in sorted(dict, key=lambda x: dict[x], reverse=True):
        print("{} -- {} times".format(word, dict[word]))


if __name__ == "__main__":
    Sum()

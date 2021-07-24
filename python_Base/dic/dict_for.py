"""
dict循环操作
"""


def handle():
    my_dict = {'name': "jack", 'age': "22", 'sex': '男'}

    # ___keys___获取key值.....默认是获取key
    for item in my_dict.keys():
        print(item)
    collection = {item for item in my_dict.keys()}
    print(collection)

    # __values___获取values值。。。
    for item in my_dict.values():
        print(item)
    collection = {item for item in my_dict.values()}
    print(collection)

    # ___items___获取key、values值
    for k, v in my_dict.items():
        print(k, v)
    collection = {item for item in my_dict.items()}
    print(collection)


# handle()

role_dic = {
    '1': 'user',
    '2': 'admin'
}
while True:
    for k in role_dic:
        print(k, role_dic[k])
    break

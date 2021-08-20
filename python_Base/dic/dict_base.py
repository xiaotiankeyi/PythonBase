'''
dict概念:
        ___values的可以是任何值、任何对象。。
        ___dict是无序的。。。
        ___dict支持del删除
        ___支持(in)判断方法
        ___key键不可变，一般是唯一的,用(数字,字符串，元祖)充当
'''


def handle():
    my_dict = {'name': "jack", 'age': "22", 'sex': '男', 'str': 'quest', 'string': 'response'}
    print(len(my_dict))  # 键值对的总数

    # ___根据序列,创建字典,并指定统一的values值
    v = dict.fromkeys(['a', 's', 'v'], 32)
    print(v)

    # ___get___根据key在字典中找values值，，找不到不报错、、、返回None
    print(my_dict.get('sds'))

    """删除字典"""
    # 根据key来删除键值对
    del my_dict["name"]
    # ___popitem___随机删除键值对
    print(my_dict.popitem())
    # ___pop___根据key来删除values,并返回被删除的values值
    print(v.pop("a"))

    """修改字典"""
    # 根据key来修改values值
    my_dict['sex'] = '女'
    print(my_dict)
    # ___update___更新列表,存在的覆盖,不存在的添加.....
    my_dict.update({'asa': 'ada'}, f=3, t=6)
    print(my_dict)

    """定义字典的keys"""
    collection = {}
    collection["name"] = " "
    collection["age"] = " "
    print(collection)


handle()

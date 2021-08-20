# 薪资计算功能
"""
要求:
从文件中取出每一条记录放入列表中,
列表的每个元素都是{'name':'egon','sex':'male','age':18,'salary':3000}的形式

2 根据1得到的列表,取出薪资最高的人的信息
3 根据1得到的列表,取出最年轻的人的信息
4 根据1得到的列表,将每个人的信息中的名字映射成首字母大写的形式
5 根据1得到的列表,过滤掉名字以a开头的人的信息
"""


def handle(file_1):
    global shop_collection
    shop_collection = []
    with open(file_1, 'r') as g:
        for i in g:
            msg = i.strip("\n").split(",")
            for v in msg:
                c = v.split()
            goods_collection = {
                "name": c[0],
                "sex": c[1],
                "age": c[2],
                "salary": c[3]}
            shop_collection.append(goods_collection)
        print('个人信息', shop_collection, )

        def maximum():
            """求出薪资最高的员工"""
            v = max(shop_collection, key=lambda x: x["salary"])
            print("薪资最高的员工是 ", v)

            def minimum():
                b = min(shop_collection, key=lambda k: k["age"])
                print("最年轻的员工是", b)

                def strip():
                    info_new = map(
                        lambda shop_collection: {
                            'name': shop_collection['name'].capitalize(),
                            'sex': shop_collection['sex'],
                            'age': shop_collection['age'],
                            'salary': shop_collection['salary']},
                        shop_collection)
                    # li = []       #第二种写法
                    # for i in f:
                    #     dic = {'name': i["name"].capitalize(), 'sex': i['sex'], 'age': i['age'], 'salary': i['salary']}
                    #     li.append(dic)
                    print("新的个人信息", list(info_new))

                    def eliminate():
                        # g=filter(lambda item:item['name'].startswith('a'),info)
                        h = []
                        for i in shop_collection:
                            if i["name"].startswith('a'):
                                enumerate
                            else:
                                h.append(i)
                        return h

                    return eliminate()

                return strip()

            return minimum()

    return maximum()


v = handle("e.txt")
print(v)

"""测试"""
f = [
    {'name': 'egon', 'sex': 'male', 'age': '18', 'salary': '3000'},
    {'name': 'alex', 'sex': 'male', 'age': '38', 'salary': '30000'},
    {'name': 'jack', 'sex': 'female', 'age': '28', 'salary': '20000'},
    {'name': 'lucy', 'sex': 'female', 'age': '28', 'salary': '10000'}
]


#
# info_new = map(lambda f: {'name': f['name'].capitalize(),
#                           'sex': f['sex'],
#                           'age': f['age'],
#                           'salary': f['salary']}, f)
# # print(list(info_new))
#
# li = []
# for i in f:
#     dic = {'name': i["name"].capitalize(), 'sex': i['sex'], 'age': i['age'], 'salary': i['salary']}
#     li.append(dic)
# # print(li)


def v():
    h = []
    for i in f:
        if i["name"].startswith('a'):
            enumerate
        else:
            h.append(i)
    return h

# m = v()
# print(m)

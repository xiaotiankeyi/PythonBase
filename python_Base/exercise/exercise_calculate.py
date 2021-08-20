# 计算功能
'''计算1—100之间的和'''
num = 1
total = 0
while num < 101:
    total = num + total
    num += 1
# print(total)

'''计算1—100之间偶数和'''
number = 1
count = 0
while number < 101:
    if number % 2 == 0:
        count = number + count
        # print(count)
    number += 1
# print(count)

'''实现有个整数加法计算机器'''
math_1 = input("请输入算式>>>> ").strip()
print(math_1.split("+"))
a, i = math_1.split("+")
a = int(a)
i = int(i)
# print(a+i)

'''计算列表中数值大小,于66来作为界限,大于的放再key_1中,小于的放再key_2中'''
list_1 = sorted([11, 22, 33, 44, 55, 66, 77, 88, 99, 90])
f = list_1.index(66)  # 先排序在获取66下标,值为(5),
dic = {"key_1": list_1[0:f], "key_2": list_1[f + 1:]}
# print(dic)


"""有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，
    将小于 66 的值保存至第二个key的值中。即：{'k1': 大于66的所有值, 'k2': 小于66的所有值}"""
num = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
dic_num = {
    "key1": [],
    "key2": []
}
for total in range(len(num)):
    if num[total] > 66:
        dic_num["key1"].append(num[total])
    else:
        dic_num["key2"].append(num[total])
# print(dic_num)

"""查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。"""
li = ["alec", " aric", "Alex", "Tony", "rain"]
for i in li:
    n = i.strip()
    if n.startswith('a') or n.startswith('A') and n.endswith('c'):
        pass
#         print(n)

"""输出商品列表，用户输入序号，显示用户选中的商品\\li = ["手机", "电脑", '鼠标垫', '游艇']"""
li = ["手机", "电脑", '鼠标垫', '游艇']
add_ram = input("输入需要添加的商品>>>>>>>>  ").strip()
li.append(add_ram)
dic = {}
# 为每个小商品添加序号
for key, li in enumerate(li, 1):
    # print(key,li)
    # 添加到字典中，序号为key，li为values
    dic.update({key: li})
print(dic)
paras = int(input("请输入序号>>>>>>  ").strip())
print(dic[paras])

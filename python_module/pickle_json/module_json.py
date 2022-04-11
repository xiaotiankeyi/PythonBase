"""
    概念:
        1、支持任何数据类型,,,,桥梁的作用
        2、规范,json字符串必须是双 " "号
        3、只要字符串属于json规范,就是json字符串
"""
import json

"""把一个字典转化为json字符串,封装成json的数据"""

# dic = {"name": "alex"}
# print(type(dic))

li = ['jack','select','changer','variables']
data = json.dumps(li)   #把列表转化为字符串

# data = json.dumps(dic)
def handle():
    print(data, type(data))
    f = open("new_file", 'a')
    f.write(data)  # 以json的形式写进文本,,,简写json.dump(dic, f)
    f.close()
# handle()

"""把文本里的字符串在以json形式取出来,转化为字典"""
r = open("new_file", "r")
order = json.loads(r.readline())
print(order, type(order))
dataa = json.loads(r.readline())  # 简写data = json.load(r)
print(data, type(dataa))

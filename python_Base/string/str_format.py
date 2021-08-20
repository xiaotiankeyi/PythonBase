# format方式格式化

tpl = "i am {} age {}".format("alex", 23)

tpl1 = "i am {2} age {0}".format("alex", 23, 45)

tpl2 = "i am {name} age {age}".format(name="alex", age="23")

"""______format()字符串格式化、基本语法是通过 {} 和 : 来代替以前的 % 。"""
print("{} {}".format("hello", "world"))  # 不指定位置，默认顺序
print("{0} {1}".format("hello", "world"))  # 设置指定位置
print("{1} {2} {1}".format("hello", "world", "hi"))  # 设置指定位置

"""#设置参数"""
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

"""#通过字典设置参数......"""
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

"""#通过列表索引设置参数"""
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

"""数字格式化"""
print("{:.2f}".format(3.1415926))  # 保留小数点后两位
print("{:+.2f}".format(3.1415926))  # 带符号保留小数点后两位

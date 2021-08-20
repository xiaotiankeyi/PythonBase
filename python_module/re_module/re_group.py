# 正则表达式之匹配分组
# | 匹配左右任意一个表达式
# (ab) 将括号里面的字符作为一个分组
# \num 引用分组num匹配到的字符串
# (?p<name>) 分组起别名
# (?p=name) 引用别名为name分组的匹配到的字符串

import re

parameter = re.match(r'[1-9]?\d$|100$', '0')
print(parameter)

num = re.match(r'[1-9]?\d$|100$', '100')
print(num)

e_mail = 'laizhitian.Bytedance.com'

b = re.search(r'\.(.*)\.', e_mail)
print(b)

number = re.match(r'(\d{3,4})-([1-9]\d{4,7})$', '010-5434457')
print(number)
print(number.group())
print(number.group(1))
print(number.group(2))
print(number.groups())
print(number.groups()[0])
print(number.groups()[1])

html = "<html><title>标题</title></html>"
parameter = r"<(.+)><(.+)>.*</.+></.+>"
l = re.match(parameter, html)
print(l)

html = "<html><title>标题</title></html>"
parameter = r"<(.+)><(.+)>.+</\2></\1>"
r = re.match(parameter, html)
print(r)

html = "<html><title>标题</title></html>"
parameter = r"<(?P<one>.+)><(?P<two>.+)>.+</(?P=two)></(?P=one)>"
l = re.match(parameter, html)
print(l)

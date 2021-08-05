# 正则表达式之匹配字符
# . 匹配任意一个字符(\n除外)
# [] 匹配列表中的字符
# \d 匹配数字0-9
# \D 匹配非数字
# \s 匹配空白字符,即空格(\n\t)
# \S 匹配非空格
# \w 匹配单词字符,即(a-z,A-Z,0-9)
# \W 匹配非单词字符

import re

val = re.match('.', 'family')
print(val)

want = re.match('[a-z]', 'played')
print(want)

d = re.match(r'\d+', '3728')
print(d)

D = re.match(r'\D', 'cc23abc')
print(D)

s = re.match(r'\s', '\n')
print(s)

S = re.match(r'\S', '1sds')
print(S)

w = re.match(r'\w+', 'sds11DA2')
print(w)

W = re.match(r'\W', '#%$')
print(W)

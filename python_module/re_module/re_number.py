# 正则表达式之表示数字

# * 匹配一个字符出现0次或者无限次(可有可无)
# + 匹配一个字符出现1次或无限次(至少一次)
# ?匹配一个字符出现一次或者0次(要么一次要么没有)
# {m} 匹配一个字符出现m次
# {m,} 匹配一个字符至少出现m次
# {m,n} 匹配一个字符出现m到n次

import re

val = re.match('[6]*', '68196263')
print(val)

aunt = re.match('[s]+', 'sister')
print(aunt)

ruler = re.match("[u]?", 'uncle')
print(ruler)

cousin = re.search('p{3}', 'ppparent')
print(cousin)

red = re.match('a{4,}', 'aaaaa')
print(red)

blue = re.match("c{3,6}", 'ccccc')
print(blue)

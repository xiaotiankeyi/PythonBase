# 正则表达式之边界
# ^ 匹配字符串开头
# $ 匹配字符串结尾
# \b 匹配一个单词的边界
# \B 匹配非单词的边界

import re

a = re.match('^a', 'aunt')
print(a)

e = re.match(r'[\w]+\suncle$', 'cousin uncle')
print(e)

b = re.match(r'.*\ber', '123 eroa')
print(b)

B = re.match(r'.*\Ber', '123 aeroa')
print(B)

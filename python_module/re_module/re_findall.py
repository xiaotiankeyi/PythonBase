# 高级用法之findall, 从左到右扫描字符串,并按照找到的顺序返回匹配,如果有多个组,则返回组列表

import re

list_val = re.findall(r'\d+', '阅读次数C:333, java:5343, python:453')
print(list_val)
print(list_val[0])
print(list_val[1])
print(list_val[2])

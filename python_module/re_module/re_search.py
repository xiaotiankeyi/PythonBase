# 高级用户之search，search扫描字符串，查找正则表达式模式产生匹配的第一个位置，
# 只返回一个匹配值，如果没有值，则返回None

import re

parameter = re.search(r'\d+', '阅读次数为99999次')
print(parameter)

# re.match方法只匹配开头的位置
# re.search

import re

params = 'hello'

string = 'good hello world'

#
# re_vales = re.match(params, string)
re_vales = re.search(params, string)


print(type(re_vales))
print(dir(re_vales))
print(re)
print('获取匹配信息:', re_vales.group())
print('获取匹配信息索引:', re_vales.span())
#  高级用法之sub， sub替换

import re

a = re.sub(r'a', 'f', 'danankdajladsa', count=2)
print('把a替换成f,替换2次:', a)


s = '阅读次数C:333, java:5343, python:453'

# 通过sub替换方式实现对上面的数字加一
def function(result):
    print(result.group())
    return str(int(result.group()) + 1)


func = re.sub(r'\d+', function, s)
print(func)

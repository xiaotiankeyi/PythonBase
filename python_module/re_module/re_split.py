# 高级用法之split用户，按照匹配规则来拆分字符串

import re

s = "he say: hello,world"
parameter = r'\s|:|,'

func = re.split(parameter, s)
print(func)

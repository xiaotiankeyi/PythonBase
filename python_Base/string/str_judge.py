'''
字符串的判断操作。。。。judge
'''

seek = 'response'
# ___isalpha___如果字符串是字母字符串，返回True，否则返回False。
print(seek.isalpha())

# ___islower___如果字符串是小写字符串，返回True，否则返回False。
print(seek.islower())

# ___isupper___如果字符串是大写字符串，返回True，否则返回False。
print(seek.isupper())

# ___isspace___如果字符串是空白字符串，返回True，否则返回False。(或空格)
print(seek.isspace())

# ___istitle___如果字符串是标题大小写字符串(首字母全部大写)，则返回True，否则返回False
print(seek.istitle())

# ___isanum___如果字符串是(字母+数字)字符串，(可以单独是数字或字符串)返回True，否则返回False。
print(seek.isalnum())

# ___isprintable___如果字符串是可打印的，返回True，否则返回False。(也可判断字符串中有不可见的内容)
print(seek.isprintable())

# ___isidentifier___如果字符串是有效的Python标识符，则返回True，否则返回False。
print(seek.isidentifier())

number = '3434'
# ___isdecimal__判断字符串中是否为数字，只能判断这种数字(3232)
print(number.isdecimal())

num = '②③④423'
# ___isdigit___如果字符串是数字字符串，返回True，否则返回False。(可以判断56②②5)
print(num.isdigit())

total = '234⑯④⑲二三'
# ___isnumeric___支持判断(234⑯④⑲二三)数字
print(total.isnumeric())

# ___title___把字符串装换为标题
title = 'Concatenate any number of strings'
vi = title.title()
print(vi, vi.istitle())


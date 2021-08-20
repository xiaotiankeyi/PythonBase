print("hello word")
name, password = "jack", "123456"
print(name)

# ___len___计算字符串的长度
print(len(name), len(password))

# ___capitalize()___首字母大写
print(name.capitalize())

coding = 'Process,finished'
# ___casefold___所有字符变小写并显示其长度
print(coding.casefold(), len(coding))

# ___count___计算's'出现多少次,从第5至9个字符中寻找
print(coding.count('s', 5, 9))

# ___endswith___已什么结尾
print(coding.endswith('d'))

# ___startswith___已什么开头
print(coding.startswith('P'))

# ___find___查找'ed'的索引，在13至16个字符之间查找.....
print(coding.find('edjj', 13, 16))

test = 'i an {name}, age {a}'
# ___format___将字符串中的占位符替换为指定的字符....____替换占位符
print(test.format(name='alex', a='18'))

# ___index___查找字符串是否存在并返回索引,找不到就报error
print(coding.index('s'))

school = 'class_student_teacher_subject'
# ____replace___(替换)把'_'替换为','能指定替换那个'_'如(2)表示替换下标为[2]的'_'
print(school.replace('_', ',', 2))
telephone = "181-7274-5976"
print(telephone.replace(telephone[0:9], "*" * 9))

# ___title___先把'_'替换为','。。在每个单词的(首字母大写)
print(school.replace('_', ',').title())

list = ['root', 'x', '0', '0', '', '/root', '/bin/bash']
# ___join___字符串被插入到每个给定字符串之间。。如':'代替了','
list_1 = ':'.join(list)
print(type(list_1), '\t\t', list_1)
a = ','
b = '23342423'
print(a.join(b))

# ___expandtabs___断句。。当字符串中有'\t'时，不够时'\t'补齐，
message = 'username\te_mail\tpassword\njack\tasdns@163.com\t123456\ntom\tasdns@163.com\t123456'
print(message.expandtabs(10))

msg = 'NET'
# ___lower___转换为(小写)
print(msg.lower())

msg_1 = 'net'
# ___upper___转化为(大写)
print(msg_1.upper())

# ------------------------------------------------------------
'''最常用的字符串操作方法。。。。
join
split
find
strip
upper
lower
replace
'''

'''
字符串的切割.....(split)
'''
info = 'root:x:0:0::/root:/bin/bash'

# ___显示索引为(1\2\3\4)的字符
print(info[0] + info[1] + info[2] + info[3])

# ___split___以冒号为切割,,在以[列表__list__]形式输入
user = info.split(':')
print(user)
# ___切割成功后,查找出'/bin/bash'的索引,,再显示列表中索引为(6)的字符
print(user.index('/bin/bash'), user[6])

english = 'price configure mock redis pinpoint share'
# ___split___默认以空格作为分隔符
print(english.split())

report = 'unique|auto increment|character|variables|enter|telnet'
# ___split('|', 3)___以'|'为分隔符,,但是以排在前面的3个'|'来切割
split_1 = report.split('|', 3)
print(split_1)
print(split_1[2])
print(split_1[0])

# # ___实例___
# while True:
#     cmd = input('>>:　').strip()
#     if len(cmd) == 0: continue
#     cmd_l = cmd.split()
#     print('命令是:%s 命令的参数是:%s' % (cmd_l[0], cmd_l[1]))

li = ['name 34 10']
# n = str(li).split()
# print(li)
for i in li:
    v = i.split()
    print(v)

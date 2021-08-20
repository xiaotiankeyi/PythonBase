'''
字符串格式化.....(%s%d).......
'''
print('\t\t\t\t__%s__代表字符串(str)也能代表数字(int)的格式化')
print('\t\t\t\t__%d__只能代表数字(int)的格式化')
print('\t\t\t\t__%f__表示接受小数类型......')
while True:
    name = input('name:')
    # print('名字是%s' % name)
    age = input('age:')
    # print('年龄是%d' % age)
    sex = input('sex:')
    # print('性别是%s' % sex)
    telephone = input('telephone:')
    # print('电话号码是%d' % telephone)

    msg = '''
            ----------%s info----------
            name:%s
            age:%s
            sex:%s
            telephone:%s
            ----------------------------
            ''' % (name, name, age, sex, telephone)
    print(msg)
    break
tpl = "i am %(name)s age %(age)d" % {"name": "alex", "age": "18"}

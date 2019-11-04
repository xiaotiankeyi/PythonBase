'''
字符串移除空白操作....(strip)
'''
response = '   review_collection   '
# ___strip___移除空白
print(response.strip())

# ___rstrip___移除右边的空白
print(response.rstrip())

# ___lstrip___移除左边的空白
print(response.lstrip())

request = '****network error@@@@@@'
# ___rstrip___移除右边的__'@'
print(request.rstrip('@'))

# ___rstrip___移除左边的__'*'
print(request.lstrip('*'))

# 例题_____移除空白的操作........
while True:
    name = input('user:').strip()
    pwd = input('password:').strip()
    if name == 'jack' and pwd == '123456':
        print('login success')
        break

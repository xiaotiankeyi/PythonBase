'''
字符串(切片)的操作
'''
index = 'response times distribution'
print(index.index('m'))

# ___查找出下标为(2—4)之间的字符串
print(index[2:5:])

# ___让字符串(倒序)显示
print(index[::-1])

# ___查询下标为(3—13)之间的字符串,步长为(2).....[start:end:步长]
print(index[3:14:2])
print(index[-5:-1])

url = "https://bpic.588ku.com/element_banner/20/19/07/abfdc337ca0d054d1416a2b61b313540.jpg"
section = url[-37:]
dir_name = "photo" + section
print(dir_name)

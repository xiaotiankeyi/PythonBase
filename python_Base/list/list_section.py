'''
列表list的切片操作.....
'''
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

# ___[::]显示列表里的所有数据
print(letter[::])

# ___[1:7:]查看列表中下标(1-6)的字符串
print(letter[1:7:])

# ___[-1::]查看列表中最后一个字符串
print(letter[-1::])

# ___[-5]从结尾往头数,显示出下标为[-5]的字符串
print(letter[-5])

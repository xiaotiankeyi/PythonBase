'''
列表(list)的增加操作.....
'''
name_list = ['jack', 'Tom', 'alex', 'eric']
# ___append___往列表中追加新的数据
name_list.append('lucy')
print(name_list)

# ___例题(循环追加)___
school = []
student = 'jack', 'Tom', 'alex', 'eric'
for total in student:
    school.append(total)
print(school)

# ___计算(1-6)之间的平方
nums = []
for num in range(1, 7):
    nums.append(num * 2)
print(nums)
# 第二种写法
number = [count * 2 for count in range(1, 7)]
print(number)

# ___计算出(0-50)之间的偶数,在计算出整个列表的长度,,再查找索引为(22)的数
even = [i for i in range(0, 50, 2)]
print(len(even), even[22])

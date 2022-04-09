num = {3, 4, 5, 7, 1, 9, 0, "request", "response"}
number = {3, 4, 5, 7, 4, 5, 65, 32, 12}

# ___set___集合的去重操作
paras = set(num)

# ___intersection___求交集,,,,两个变量都存在
num.intersection(number)
print(set(num) & set(number))

# ___union___求并集,,,,,把两个变量的元素相加,,,,去重复
num.union(number)
print(number | number)

# ___difference___差集(下面的代码只显示存在于num集合中的且和number没有相同的元素,....)
print(num - number)
num.difference(number)

# ___symmetric_difference____交叉补集,去重复
num.symmetric_difference(number)
print(num ^ number)

# ___isdisjoint___求证是num和number交集是否为空,为空就表示没有重复的,返回True
print(num.isdisjoint(number))

# ___update____更新多个值用update.....
num.update(number)

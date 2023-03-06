'''
集合概念:
    1、不同元素组成
    2、无序
    3、不能存在重复的
    4、可变类型,只能定义(str,int,tuple)
    3、集合支持for循环
'''
num = {3, 4, 5, 7, 1, 9, 0, "request", "response"}

# for i in num:
#     print(i)

# ___add___往集合里面添加一个字符
num.add(2)

# ___clear___清空集合
# num.clear()

# ___copy___复制集合
sum = num.copy()

# ___pop___删除(随机删除)
print('返回删除的值', num.pop())

# ___remove___指定字符删除,不存在就报error
num.remove(2)

# ___discard___指定字符删除,不存在不会受到影响
num.discard("request")

# ___set___集合的去重操作
paras = set(num)

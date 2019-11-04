"""
匿名函数lambda
"""


def change(x):
    return x + "age"


res = change("name")
print(res)

index_1 = lambda x: x + "age"
res = index_1("name")
print(res)

# Generator 与控制流  关键yield的使用

def generator():
    print('before')
    yield  # break 1
    print('middle')
    yield  # break 2
    print('after')


x = generator()

# next(x)     # ==>before
# next(x)     # ==>middle
# next(x)     # ==>after

# send的使用
def result():
    print('开始执行....')
    val = yield 44
    print('接收send传回的值：', val)
    yield 33


g = result()
h = g.__next__()
print(h)
h = g.send('发送给yield')
print(h)
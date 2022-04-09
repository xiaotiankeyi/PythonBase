"""
函数是第一类对象,即函数可以当做数据传递
    1、可以被应用
    2、可以当做参数传递
    3、返回值可以是函数
    4、可以当做容器类型的元祖
"""


def foo():
    print('foo')
    print('foo_1')


def bar():
    print('bar')


dic = {
    'foo': foo,
    'bar': bar,
}
while True:
    choice = input('>>: ').strip()
    if choice in dic:
        dic[choice]()

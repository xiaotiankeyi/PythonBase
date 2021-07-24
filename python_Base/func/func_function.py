"""
特性：
    1、不可变、不应变量保存转态、不修改变量
    2、函数名可以当做参数传递
    3、返回值可以是函数名
    4、第一类变量,函数及变量

高阶函数的定义：
    1、传递的参数是一个函数名
    2、返回的参数是一个函数名

"""
"""把函数当做参数传给例外一个函数"""


def foo(n):
    print(n)


def bar(name):
    print("my name is %s" % name)
    return 1


foo(bar)  # 显示出函数bar的地址........
foo(bar("alex"))

"""返回值中包含函数"""


def bar():
    print("from bar")


def foo():
    print("from foo")
    return bar


n = foo()
n()

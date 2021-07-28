"""
函数作用域概念：
    1、一个标识符的可见范围，这就是标识符的作用域。一般常说的是变量的作用域
    2、全局作用域（global）：在整个程序运行环境中都可见
    3、局部作用域：在函数、类等内部可见；局部变量使用范围不能超过其所在的局部作用域
"""
"""global方法,把name修改为全局变量,下面在调用name时都为'jack'...."""
name = "alex"


def paras():
    # global name
    name = "jack"

    def accept():
        print(name)

    accept()


paras()
print(name)

"""global全局变量"""
name = "刚娘"


def collection():
    name = "陈卓"

    def accept():
        global name
        name = "冷静"

    accept()
    print(name)


print(name)
collection()
print(name)

# """nonlocal修改上级变量"""
name = "刚娘"


def collection():
    name = "陈卓"

    def accept():
        """内部函数修改外部函数的变量"""
        nonlocal name
        name = "冷静"

    accept()
    print(name)


print(name)
collection()
print(name)

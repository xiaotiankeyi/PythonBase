# 闭包
#  应用，在不改变原码的前提下，为现有函数添加新的功能

import time


def one(num1):
    """闭包的形式,写法"""
    def two(num2):
        # 如果要修改外部函数的参数
        # nonlocal num1
        # num1 = 5
        return num2 + num1
    return two


def logInfo(func):
    """增加新的功能"""
    try:
        with open(file='log.txt', mode='a', encoding='utf-8') as f:
            f.write(func.__name__)
            f.write('\t')
            f.write(time.asctime())
            f.write('\n')
    except BaseException as e:
        print(e)

    finally:
        f.close()


def ruler(func):
    """闭包功能"""
    def funcIN():
        logInfo(func)       # 先运行添加的新功能
        func()
    return funcIN


def login():
    print("运行登录功能。。。。。")


if __name__ == "__main__":
    a = one(10)
    print('a.__name__', a.__name__)
    print(type(a), a)
    val = a(20)
    print(val)
    # funcin = ruler(login)
    # print('func_name:', funcin.__name__)
    # funcin()

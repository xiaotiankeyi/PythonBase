# wraps函数应用于装饰器配合使用
# 作用是会把原函数的信息复制给包装的函数对象

from functools import wraps

def family(function):
    @wraps(function)
    def func(*args, **kwargs):
        print("运行的函数是:{}".format(func.__name__))
        return function(*args, **kwargs)

    return func


@family
def parent():
    """被装饰得函数！！！"""
    print('========')


if __name__ == "__main__":
    parent()
    print(parent.__doc__)

